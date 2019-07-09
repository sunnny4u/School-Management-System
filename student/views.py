from django.shortcuts import render,redirect
from .models import StudentInfo,DistrictInfo,UpazilaInfo,ShopInfo

# Create your views here.



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
