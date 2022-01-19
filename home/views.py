from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_sameorigin

import datetime

from django.views.generic import CreateView

from trees.models import Tree
from .models import Search
from upload.models import Upload

# Create your views here.


# class BaseView(View):
#     template_name = 'base/base.html'
#
#     def get(self, request):
#
#         time_update = Upload.objects.all().order_by('-time_now')[0].time_now
#         request.session['time'] = str(time_update)
#         time_session = request.session.get('time')
#
#         context = {'time': time_update, 'time_session': time_session}
#         return render(request, self.template_name, context)


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        # THIS FIRST UPDATE THE SESSION
        time_update = Upload.objects.all().order_by('-time_now')[0].time_now
        print(type(time_update))
        count_update = Upload.objects.values()
        cont = []
        for val in count_update:
            cont.append(val['tree_count'])
        total = sum(cont)
        request.session['time'] = str(time_update)
        request.session['counter'] = str(total)
        # THEN AFTER IT PROCESS THE NORMAL VIEWS FOR THE SEARCH AND ALL

        # tree_list = Tree.objects.all()
        search = request.GET.get('search') if request.GET.get('search') is not None else ''
        search_tree = Tree.objects.filter(
            Q(scientific_name__icontains=search) |
            Q(local_name__icontains=search) |
            Q(common_name__icontains=search)
        )

        # THIS BELOW IS KIND OF MESSING EVERYTHING ON THE HOME SEARCH, I MIGHT REMOVE IT
        search_place = Upload.objects.filter(
            Q(location_name__icontains=search)
        )

        context = {
            'search_tree': search_tree,
            'search': search,
            'search_place': search_place
        }

        return render(request, self.template_name, context)


class SpecificSearch(View):
    template_name = 'home/specific_search.html'

    def get(self, request, pk):

        # THIS WILL QUERY AND RETURN ALL THE SEARCHABLE OPTIONS IN THE DATABASE(NAMES, LOCATION AND COORDINATES) AND
        # THEN UPDATE THE CONTEXT VARIABLE
        search_option = Search.objects.all()
        context = {'search_options': search_option}

        # THIS WILL LOOP THROUGH ALL THE SEARCHABLE RETURNED BY SEARCH OPTION AND THEN CHECK THE PK OF THE URL AND THEN
        # HOLD THE VALUE WHICH WAS CLICKED BY THE USER FOR SEARCH
        for search_item in search_option:
            if pk == search_item.id:
                search = request.GET.get('specific_search') if request.GET.get('specific_search') is not None else ''

                context.update({'search': search})

                search_key = Search.objects.get(id=pk).search_by
                # THIS WILL SET TO NULL FIRST THEN RE-ASSIGN THEN LATER IF THE "IF CONDITION" IS MET
                search_tree = None
                search_place = None
                search_cont = None

                # THIS WILL CHECK THE PK VALUE WHICH TALLIES WITH WHAT THE USER CLICKED AND THEN USE CONDITIONAL
                # STATEMENT TO KNOW THE SEARCH-BY VALUES SO AS TO KNOW WHERE TO QUERY IN THE TREE DATABASE
                # DEPENDING ON WHAT THE USER CLICKED
                # AFTER THEN THE CONTEXT VARIABLE WILL BE UPDATED
                if search_key == 'scientific_name':
                    search_tree = Tree.objects.filter(
                        Q(scientific_name__icontains=search)
                    )

                elif search_key == 'local_name':
                    search_tree = Tree.objects.filter(
                        Q(local_name__icontains=search)
                    )

                elif search_key == 'common_name':
                    search_tree = Tree.objects.filter(
                        Q(common_name__icontains=search)
                    )

                # THIS WILL GET THE LOCATION SEARCHED BY THE SEARCH VARIABLE AND THE RUN IT THROUGH THE UPLOAD
                # MODEL AND THEN RETURN THE TREES AROUND THAT AREA
                elif search_key == 'location_name':
                    search_place = Upload.objects.filter(
                        Q(location_name__icontains=search)
                    )

                elif search_key == 'coordinates':
                    try:
                        if type(float(search[0:4])) == float:
                            long_lat = search.split(",")
                            lat = float(long_lat[0])
                            long = float(long_lat[1])
                            upload_db = Upload.objects.all()
                            search_cont = []
                            for item in upload_db:
                                try:
                                    item_lat = float(item.latitude)
                                    item_long = float(item.longitude)
                                    if abs(lat - item_lat) <= 0.025 and abs(long - item_long) <= 0.015:
                                        search_cont.append(item)
                                    context.update({'search_coord': search_cont})
                                except:
                                    pass
                    except:
                        pass
                context.update({'search_item': search_item})

                # THIS CHECKS IF THE QUERYSET OF THE TREES IS EMPTY OR NOT SO AS TO KNOW WHAT TO TEMPLATE OUT
                if not search_tree and not search_place and not search_cont:
                    context.update({'search_error': 'There are no suggestions'})
                else:
                    context.update({'search_tree': search_tree})
                    context.update({'search_place': search_place})

        return render(request, self.template_name, context)


class TreeDetails(View):
    template_name = 'home/tree_details.html'

    def get(self, request, pk):
        tree_info = Tree.objects.get(id=pk)

        # THIS BELOW THE SEARCHED TREE AND RETURN LOCATIONS WHERE FOUND
        tree_locations = Upload.objects.filter(tree_name__scientific_name=tree_info.scientific_name)

        context = {
            'tree_info': tree_info,
            'tree_location': tree_locations
        }
        return render(request, self.template_name, context)


class TreeLocationPicture(View):
    template_name = 'home/tree_picture.html'

    # THIS SET THE X_FRAME_OPTIONS = 'SAMEORIGIN' BECAUSE DJANGO PREVENT CLICKJACKING
    @xframe_options_sameorigin
    def get(self, request, pk):
        result = Upload.objects.get(id=pk)
        picture = result.tree_picture
        picture2 = result.tree_picture2
        picture3 = result.tree_picture3
        coord = result.coordinates
        desc = result.location_description

        context = {
            'pictures': [picture, picture2, picture3],
            'description': desc
        }
        try:
            if type(float(coord[0:4])) == float:
                context.update({'coordinate': coord})
        except:
            pass

        return render(request, self.template_name, context)


class TreeLocationDetails(View):
    template_name = 'home/tree_location_details.html'

    def get(self, request, pk):

        result = Upload.objects.get(id=pk)
        location_scientific_name = result.tree_name
        tree_info = Tree.objects.get(scientific_name=location_scientific_name)

        context = {'result': result, 'tree_info': tree_info}
        return render(request, self.template_name, context)


class Pharmacological(View):
    template_name = 'home/pharmacological.html'

    def get(self, request, pk):
        tree_pharm_info = Tree.objects.get(id=pk).pharmacological_details

        context = {'tree_pharm_info': tree_pharm_info}
        return render(request, self.template_name, context)


