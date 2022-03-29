from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils import timezone

from django.views.generic import CreateView, UpdateView

from trees.models import Tree
from .models import Search
from upload.models import Upload
from .models import Contributor
from .forms import ProfileFrom

from utilities.sequence_sort import mysorttree, mysortplace


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
        try:
            # THIS FIRST UPDATE THE SESSION
            # IT RETURNS THE NUMBER OF OBJECTS IN UPLOAD DATABASE
            # total = Upload.objects.count()
            # request.session['counter'] = str(total)

            time_update = Upload.objects.all().order_by('-time_now')[0].time_now
            str_date = time_update.strftime("%Y-%m-%d %H:%M:%S")
            # local_dt = timezone.localtime(time_update)
            # print(local_dt)

            cont_update = Upload.objects.values()
            cont = []
            for val in cont_update:
                cont.append(val['tree_count'])
            total = sum(cont)
            request.session['time'] = str(str_date)
            request.session['counter'] = str(total)
        except:
            pass
            # THEN AFTER IT PROCESS THE NORMAL VIEWS FOR THE SEARCH AND ALL

        # tree_list = Tree.objects.all()
        context = {}
        search = request.GET.get('q', '')

        # THIS CHECK IF THE SEARCH IS AN EMPTY STRING
        # IF SO IT WILL RETURN THE PAGE LIKE THAT, BECAUSE WE DO NOT WANT TO RETURN ALL THE DATA IN THE DATABASE
        # IF WE QUERY WITH AN EMPTY STRING
        if search == '':
            return render(request, self.template_name, context)

        search_tree_tree = Tree.objects.filter(
            Q(scientific_name__icontains=search) |
            Q(local_name__icontains=search) |
            Q(common_name__icontains=search)
        )

        search_tree_upload = Upload.objects.filter(
            Q(tree_name__scientific_name__icontains=search) |
            Q(tree_name__local_name__icontains=search) |
            Q(tree_name__common_name__icontains=search)
        )
        search_tree = set()
        for x in search_tree_tree:
            for y in search_tree_upload:
                if x.scientific_name == y.tree_name.scientific_name:
                    search_tree.add(x)
        # set_tree_count = len(search_tree)

        # THIS BELOW IS KIND OF MESSING EVERYTHING ON THE HOME SEARCH, I MIGHT REMOVE IT
        search_place = Upload.objects.filter(
            Q(location_name__icontains=search)
        )
        # search_place_count = search_place.count()
        # total_len = set_tree_count + search_place_count

        # PAGINATORS
        # THIS BELOW SORT THE DISORGANIZED SET PASSED FROM MODEL WITH A FUNCTION IN UTILITIES
        # IT FIRST CONVERTS IT INTO LIST AND THEN PERFORM THE SORT FUNCTION AND THE PASS IT TO THE PAGINATOR
        list_search_tree = list(search_tree)
        list_search_tree.sort(key=mysorttree)
        list_search_place = list(search_place)
        list_search_place.sort(key=mysortplace)

        search_tree_place = list_search_tree + list_search_place

        paginator = Paginator(search_tree_place, 30)
        page_number = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {
            'search_result': page_obj,
            'search': str(search),
            # 'total_len': total_len,
            # 'page_number': int(page_number)
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
                search = request.GET.get('q', '')

                # context.update({'search': search})
                context.update({'search_item': search_item})

                # THIS CHECK IF THE SEARCH IS AN EMPTY STRING
                # IF SO IT WILL RETURN THE PAGE LIKE THAT, BECAUSE WE DO NOT WANT TO RETURN ALL THE DATA IN THE DATABASE
                # IF WE QUERY WITH AN EMPTY STRING
                if search == '':
                    return render(request, self.template_name, context)

                search_key = Search.objects.get(id=pk).search_by
                # THIS WILL SET TO NULL FIRST THEN RE-ASSIGN THEN LATER IF THE "IF CONDITION" IS MET
                search_tree = None
                search_place = None
                search_cont = None

                # THIS WILL CHECK THE PK VALUE WHICH TALLIES WITH WHAT THE USER CLICKED AND THEN USE CONDITIONAL
                # STATEMENT TO KNOW THE SEARCH-BY VALUES TO KNOW WHERE TO QUERY IN THE TREE DATABASE
                # DEPENDING ON WHAT THE USER CLICKED
                # AFTER THEN THE CONTEXT VARIABLE WILL BE UPDATED
                if search_key == 'scientific_name':
                    search_tree_tree = Tree.objects.filter(
                        Q(scientific_name__icontains=search)
                    )

                    search_tree_upload = Upload.objects.filter(
                        Q(tree_name__scientific_name__icontains=search)
                    )
                    search_tree = set()
                    for x in search_tree_tree:
                        for y in search_tree_upload:
                            if x.scientific_name == y.tree_name.scientific_name:
                                search_tree.add(x)

                    # PAGINATORS
                    search_tree = list(search_tree)
                    search_tree.sort(key=mysorttree)

                    paginator = Paginator(search_tree, 30)
                    page_number = request.GET.get('page', 1)
                    try:
                        page_obj = paginator.page(page_number)
                    except PageNotAnInteger:
                        page_obj = paginator.page(1)
                    except EmptyPage:
                        page_obj = paginator.page(paginator.num_pages)

                    context.update({
                        'search_tree': True,
                        'search_result': page_obj,
                        'search': str(search)
                    })

                elif search_key == 'local_name':
                    search_tree_tree = Tree.objects.filter(
                        Q(local_name__icontains=search)
                    )

                    search_tree_upload = Upload.objects.filter(
                        Q(tree_name__local_name__icontains=search)
                    )
                    search_tree = set()
                    for x in search_tree_tree:
                        for y in search_tree_upload:
                            if x.scientific_name == y.tree_name.scientific_name:
                                search_tree.add(x)

                    # PAGINATORS
                    search_tree = list(search_tree)
                    search_tree.sort(key=mysorttree)

                    paginator = Paginator(search_tree, 30)
                    page_number = request.GET.get('page', 1)
                    try:
                        page_obj = paginator.page(page_number)
                    except PageNotAnInteger:
                        page_obj = paginator.page(1)
                    except EmptyPage:
                        page_obj = paginator.page(paginator.num_pages)

                    context.update(
                        {
                            'search_tree': True,
                            'search_result': page_obj,
                            'search': str(search)
                        })

                elif search_key == 'common_name':
                    search_tree_tree = Tree.objects.filter(
                        Q(common_name__icontains=search)
                    )

                    search_tree_upload = Upload.objects.filter(
                        Q(tree_name__common_name__icontains=search)
                    )
                    search_tree = set()
                    for x in search_tree_tree:
                        for y in search_tree_upload:
                            if x.scientific_name == y.tree_name.scientific_name:
                                search_tree.add(x)

                    # PAGINATORS
                    search_tree = list(search_tree)
                    search_tree.sort(key=mysorttree)

                    paginator = Paginator(search_tree, 30)
                    page_number = request.GET.get('page', 1)
                    try:
                        page_obj = paginator.page(page_number)
                    except PageNotAnInteger:
                        page_obj = paginator.page(1)
                    except EmptyPage:
                        page_obj = paginator.page(paginator.num_pages)

                    context.update({
                        'search_tree': True,
                        'search_result': page_obj,
                        'search': str(search)
                    })

                # THIS WILL GET THE LOCATION SEARCHED BY THE SEARCH VARIABLE AND THE RUN IT THROUGH THE UPLOAD
                # MODEL AND THEN RETURN THE TREES AROUND THAT AREA
                elif search_key == 'location_name':
                    search_place = Upload.objects.filter(
                        Q(location_name__icontains=search)
                    )

                    # PAGINATORS
                    paginator = Paginator(search_place, 30)
                    page_number = request.GET.get('page', 1)
                    try:
                        page_obj = paginator.page(page_number)
                    except PageNotAnInteger:
                        page_obj = paginator.page(1)
                    except EmptyPage:
                        page_obj = paginator.page(paginator.num_pages)

                    context.update({
                        'search_place': True,
                        'search_result': page_obj,
                        'search': str(search)
                    })

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
                                    if abs(lat - item_lat) <= 0.0005 and abs(long - item_long) <= 0.0015:
                                        search_cont.append(item)

                                    # PAGINATORS
                                    paginator = Paginator(search_cont, 3)
                                    page_number = request.GET.get('page', 1)
                                    try:
                                        page_obj = paginator.page(page_number)
                                    except PageNotAnInteger:
                                        page_obj = paginator.page(1)
                                    except EmptyPage:
                                        page_obj = paginator.page(paginator.num_pages)

                                    context.update({
                                        'search_coord': True,
                                        'search_result': page_obj,
                                        'search': str(search)
                                    })
                                except:
                                    pass
                    except:
                        pass

                # THIS CHECKS IF THE QUERYSET OF THE TREES IS EMPTY OR NOT SO AS TO KNOW WHAT TO TEMPLATE OUT
                if not search_tree and not search_place and not search_cont:
                    context.update({'search_error': 'There are no suggestions'})
                else:
                    pass

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
        genus_specie = result.tree_name.genus_specie
        health = result.health_status
        uploader = result.uploader

        context = {
            'pictures': [picture, picture2, picture3],
            'description': desc,
            'genus_specie': genus_specie,
            'health': health,
            'uploader': uploader
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
        genus_specie = result.tree_name.genus_specie

        context = {'result': result, 'tree_info': tree_info, 'genus_specie': genus_specie}
        return render(request, self.template_name, context)


class Pharmacological(View):
    template_name = 'home/pharmacological.html'

    def get(self, request, pk):
        tree_pharm_info = Tree.objects.get(id=pk).pharmacological_details

        context = {'tree_pharm_info': tree_pharm_info}
        return render(request, self.template_name, context)


class TreeContributor(View):
    template_name = 'home/contributors.html'

    def get(self, request):
        contributors = Contributor.objects.all()
        context = {
            'contributors': contributors
        }
        return render(request, self.template_name, context)


class Profile(LoginRequiredMixin, UpdateView):
    model = Contributor
    # fields = '__all__'
    # form_class = UserForm
    form_class = ProfileFrom
    success_url = reverse_lazy('home:home')
    template_name = 'home/contributor_form.html'

    def form_valid(self, form):
        current_user = User.objects.get(username=self.request.user.username)
        form.instance.user = current_user
        return super(Profile, self).form_valid(form)

    # def get(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     context = {
    #         'user': user,
    #         'form': self.form_class,
    #         'form2': self.form_class2
    #     }
    #     return render(request, self.template_name, context)


def how_to_use(request):
    return render(request, 'home/how_to_use.html')


def about(request):
    return render(request, 'home/about.html')


def acknowledgement(request):
    return render(request, 'home/acknowledgement.html')
