
from django.shortcuts import render,redirect,get_object_or_404

from .models import StudentInfo,DistrictInfo,UpazilaInfo,ShopInfo
from .forms import Listform
from django.contrib import messages

# Create your views here.


def shop_info(request):
	all_shop = ShopInfo.objects.all()
	context = {'shop':all_shop}
	return render(request, 'student/shop_list.html',context)


def student_list(request):
	all_student = StudentInfo.objects.all()
	context = { 'student':all_student}
	return render(request,'student/index.html',context)


def district_info(request):
	all_district = DistrictInfo.objects.all()
	context = {'district':all_district}
	return render(request,'student/district_list.html',context)


def upazila_info(request):
	all_upazila = UpazilaInfo.objects.all()
	context = {'upazila':all_upazila}
	return render(request,'student/upazila_list.html',context)



def shop_info(request):
	all_shop = ShopInfo.objects.all()
	context = {'shop':all_shop}
	return render(request,'student/shop_list.html',context)

def shop_filter(request,ShopName):
	shop_filt = ShopInfo.objects.filter(rent=ShopName)
	context = {'shop':shop_filt}
	return render(request,'student/shop_list.html',context)


def create(request):
	print(request.POST)
	shopname = request.GET['shopname']
	rent = request.GET['rent']
	paidrent = request.GET['paidrent']
	comments = request.GET['comments']

	msi = ShopInfo(shopname=shopname, rent=rent, paidrent=paidrent, comments=comments)
	msi.save()
	return redirect('/')




def district_filter(request,name):
	district_filt = DistrictInfo.objects.filter(division=name)
	context = {'district':district_filt}
	return render(request,'student/district_filter.html',context)


def edit_post(request,post_id):
	if request.method == 'POST':
		comments = ShopInfo.objects.get(pk=post_id)
		form = Listform(request.POST or None, instance=comments)
		if form.is_valid():
			form.save()
		messages.success(request,'Message updated..!')
		return redirect('shop_info')
		
	else:
		single_shop = ShopInfo.objects.get(pk=post_id)
		context = {'s_shop':single_shop}
		return render(request,'edit.html',context)


