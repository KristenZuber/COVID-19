from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import (
Alabama,
Alaska,
Arizona,
Arkansas,
California,
Colorado,
Connecticut,
Delaware,
Florida,
Georgia,
Hawaii,
Idaho,
Illinois,
Indiana,
Iowa,
Kansas,
Kentucky,
Louisiana,
Maine,
Maryland,
Massachusetts,
Michigan,
Minnesota,
Mississippi,
Missouri,
Montana,
Nebraska,
Nevada,
NewHampshire,
NewJersey,
NewMexico,
NewYork,
NorthCarolina,
NorthDakota,
Ohio,
Oklahoma,
Oregon,
Pennsylvania,
RhodeIsland,
SouthCarolina,
SouthDakota,
Tennessee,
Texas,
Utah,
Vermont,
Virginia,
Washington,
WestVirginia,
Wisconsin,
Wyoming,
)

# Create your views here.
# class USAListView(ListView):
#     template_name = 'graphs/usa.html'
#     context_object_name = 'usa'
#
# class GeorgiaListView(ListView):
#     template_name = 'graphs/georgia.html'
#     context_object_name = 'georgia'
#
# class PredictionsListView(ListView):
#     template_name = 'graphs/predictions.html'
#     context_object_name = 'predictions'

def home(request):
    return render(request, 'graphs/home.html')

def info(request):
    template_name = 'graphs/info.html'
    return render(request, 'graphs/info.html')

def conclusion(request):
    template_name = 'graphs/conclusion.html'
    return render(request, 'graphs/conclusion.html')

class AlabamaListView(ListView):
    model = Alabama
    template_name = 'graphs/alabama.html'
    context_object_name = 'alabama'

def alabama(request):
    template_name = 'graphs/alabama.html'
    context = {
        'alabama': Alabama.objects.all()
    }
    return render(request, 'graphs/alabama.html', context)

class AlaskaListView(ListView):
    model = Alaska
    template_name = 'graphs/alaska.html'
    context_object_name = 'alaska'

def alaska(request):
    template_name = 'graphs/alaska.html'
    context = {
        'alaska': Alaska.objects.all()
    }
    return render(request, 'graphs/alaska.html', context)

class ArizonaListView(ListView):
    model = Arizona
    template_name = 'graphs/arizona.html'
    context_object_name = 'arizona'

def arizona(request):
    template_name = 'graphs/arizona.html'
    context = {
        'arizona': Arizona.objects.all()
    }
    return render(request, 'graphs/arizona.html', context)

class ArkansasListView(ListView):
    model = Arkansas
    template_name = 'graphs/arkansas.html'
    context_object_name = 'arkansas'

def arkansas(request):
    template_name = 'graphs/arkansas.html'
    context = {
        'arkansas': Arkansas.objects.all()
    }
    return render(request, 'graphs/arkansas.html', context)

class CaliforniaListView(ListView):
    model = California
    template_name = 'graphs/california.html'
    context_object_name = 'california'

def california(request):
    template_name = 'graphs/california.html'
    context = {
        'california': California.objects.all()
    }
    return render(request, 'graphs/california.html', context)

class ColoradoListView(ListView):
    model = Colorado
    template_name = 'graphs/colorado.html'
    context_object_name = 'colorado'

def colorado(request):
    template_name = 'graphs/colorado.html'
    context = {
        'colorado': Colorado.objects.all()
    }
    return render(request, 'graphs/colorado.html', context)

class ConnecticutListView(ListView):
    model = Connecticut
    template_name = 'graphs/connecticut.html'
    context_object_name = 'connecticut'

def connecticut(request):
    template_name = 'graphs/connecticut.html'
    context = {
        'connecticut': Connecticut.objects.all()
    }
    return render(request, 'graphs/connecticut.html', context)

class DelawareListView(ListView):
    model = Delaware
    template_name = 'graphs/delaware.html'
    context_object_name = 'delaware'

def delaware(request):
    template_name = 'graphs/delaware.html'
    context = {
        'delaware': Delaware.objects.all()
    }
    return render(request, 'graphs/delaware.html', context)

class FloridaListView(ListView):
    model = Florida
    template_name = 'graphs/florida.html'
    context_object_name = 'florida'

def florida(request):
    template_name = 'graphs/florida.html'
    context = {
        'florida': Florida.objects.all()
    }
    return render(request, 'graphs/florida.html', context)

class GeorgiaListView(ListView):
    model = Georgia
    template_name = 'graphs/georgia.html'
    context_object_name = 'georgia'

def georgia(request):
    template_name = 'graphs/georgia.html'
    context = {
        'georgia': Georgia.objects.all()
    }
    return render(request, 'graphs/georgia.html', context)

class HawaiiListView(ListView):
    model = Hawaii
    template_name = 'graphs/hawaii.html'
    context_object_name = 'hawaii'

def hawaii(request):
    template_name = 'graphs/hawaii.html'
    context = {
        'hawaii': Hawaii.objects.all()
    }
    return render(request, 'graphs/hawaii.html', context)

class IdahoListView(ListView):
    model = Idaho
    template_name = 'graphs/idaho.html'
    context_object_name = 'idaho'

def idaho(request):
    template_name = 'graphs/idaho.html'
    context = {
        'idaho': Idaho.objects.all()
    }
    return render(request, 'graphs/idaho.html', context)

class IllinoisListView(ListView):
    model = Illinois
    template_name = 'graphs/illinois.html'
    context_object_name = 'illinois'

def illinois(request):
    template_name = 'graphs/illinois.html'
    context = {
        'illinois': Illinois.objects.all()
    }
    return render(request, 'graphs/illinois.html', context)

class IndianaListView(ListView):
    model = Indiana
    template_name = 'graphs/indiana.html'
    context_object_name = 'indiana'

def indiana(request):
    template_name = 'graphs/indiana.html'
    context = {
        'indiana': Indiana.objects.all()
    }
    return render(request, 'graphs/indiana.html', context)

class IowaListView(ListView):
    model = Iowa
    template_name = 'graphs/iowa.html'
    context_object_name = 'iowa'

def iowa(request):
    template_name = 'graphs/iowa.html'
    context = {
        'iowa': Iowa.objects.all()
    }
    return render(request, 'graphs/iowa.html', context)

class KansasListView(ListView):
    model = Kansas
    template_name = 'graphs/kansas.html'
    context_object_name = 'kansas'

def kansas(request):
    template_name = 'graphs/kansas.html'
    context = {
        'kansas': Kansas.objects.all()
    }
    return render(request, 'graphs/kansas.html', context)

class KentuckyListView(ListView):
    model = Kentucky
    template_name = 'graphs/kentucky.html'
    context_object_name = 'kentucky'

def kentucky(request):
    template_name = 'graphs/kentucky.html'
    context = {
        'kentucky': Kentucky.objects.all()
    }
    return render(request, 'graphs/kentucky.html', context)

class LouisianaListView(ListView):
    model = Louisiana
    template_name = 'graphs/louisiana.html'
    context_object_name = 'louisiana'

def louisiana(request):
    template_name = 'graphs/louisiana.html'
    context = {
        'louisiana': Louisiana.objects.all()
    }
    return render(request, 'graphs/louisiana.html', context)

class MaineListView(ListView):
    model = Maine
    template_name = 'graphs/maine.html'
    context_object_name = 'maine'

def maine(request):
    template_name = 'graphs/maine.html'
    context = {
        'maine': Maine.objects.all()
    }
    return render(request, 'graphs/maine.html', context)

class MarylandListView(ListView):
    model = Maryland
    template_name = 'graphs/maryland.html'
    context_object_name = 'maryland'

def maryland(request):
    template_name = 'graphs/maryland.html'
    context = {
        'maryland': Maryland.objects.all()
    }
    return render(request, 'graphs/maryland.html', context)

class MassachusettsListView(ListView):
    model = Massachusetts
    template_name = 'graphs/massachusetts.html'
    context_object_name = 'massachusetts'

def massachusetts(request):
    template_name = 'graphs/massachusetts.html'
    context = {
        'massachusetts': Massachusetts.objects.all()
    }
    return render(request, 'graphs/massachusetts.html', context)

class MichiganListView(ListView):
    model = Michigan
    template_name = 'graphs/michigan.html'
    context_object_name = 'michigan'

def michigan(request):
    template_name = 'graphs/michigan.html'
    context = {
        'michigan': Michigan.objects.all()
    }
    return render(request, 'graphs/michigan.html', context)

class MinnesotaListView(ListView):
    model = Minnesota
    template_name = 'graphs/minnesota.html'
    context_object_name = 'minnesota'

def minnesota(request):
    template_name = 'graphs/minnesota.html'
    context = {
        'minnesota': Minnesota.objects.all()
    }
    return render(request, 'graphs/minnesota.html', context)

class MississippiListView(ListView):
    model = Mississippi
    template_name = 'graphs/mississippi.html'
    context_object_name = 'mississippi'

def mississippi(request):
    template_name = 'graphs/mississippi.html'
    context = {
        'mississippi': Mississippi.objects.all()
    }
    return render(request, 'graphs/mississippi.html', context)

class MissouriListView(ListView):
    model = Missouri
    template_name = 'graphs/missouri.html'
    context_object_name = 'missouri'

def missouri(request):
    template_name = 'graphs/missouri.html'
    context = {
        'missouri': Missouri.objects.all()
    }
    return render(request, 'graphs/missouri.html', context)

class MontanaListView(ListView):
    model = Montana
    template_name = 'graphs/montana.html'
    context_object_name = 'montana'

def montana(request):
    template_name = 'graphs/montana.html'
    context = {
        'montana': Montana.objects.all()
    }
    return render(request, 'graphs/montana.html', context)

class NebraskaListView(ListView):
    model = Nebraska
    template_name = 'graphs/nebraska.html'
    context_object_name = 'nebraska'

def nebraska(request):
    template_name = 'graphs/nebraska.html'
    context = {
        'nebraska': Nebraska.objects.all()
    }
    return render(request, 'graphs/nebraska.html', context)

class NevadaListView(ListView):
    model = Nevada
    template_name = 'graphs/nevada.html'
    context_object_name = 'nevada'

def nevada(request):
    template_name = 'graphs/nevada.html'
    context = {
        'nevada': Nevada.objects.all()
    }
    return render(request, 'graphs/nevada.html', context)

class NewHampshireListView(ListView):
    model = NewHampshire
    template_name = 'graphs/new-hampshire.html'
    context_object_name = 'newhampshire'

def new_hampshire(request):
    template_name = 'graphs/new-hampshire.html'
    context = {
        'newhampshire': NewHampshire.objects.all()
    }
    return render(request, 'graphs/new-hampshire.html', context)

class NewJerseyListView(ListView):
    model = NewJersey
    template_name = 'graphs/new-jersey.html'
    context_object_name = 'newjersey'

def new_jersey(request):
    template_name = 'graphs/new-jersey.html'
    context = {
        'newjersey': NewJersey.objects.all()
    }
    return render(request, 'graphs/new-jersey.html', context)

class NewMexicoListView(ListView):
    model = NewMexico
    template_name = 'graphs/new-mexico.html'
    context_object_name = 'newmexico'

def new_mexico(request):
    template_name = 'graphs/new-mexico.html'
    context = {
        'newmexico': NewMexico.objects.all()
    }
    return render(request, 'graphs/new-mexico.html', context)

class NewYorkListView(ListView):
    model = NewYork
    template_name = 'graphs/new-york.html'
    context_object_name = 'newyork'

def new_york(request):
    template_name = 'graphs/new-york.html'
    context = {
        'newyork': NewYork.objects.all()
    }
    return render(request, 'graphs/new-york.html', context)

class NorthCarolinaListView(ListView):
    model = NorthCarolina
    template_name = 'graphs/north-carolina.html'
    context_object_name = 'northcarolina'

def north_carolina(request):
    template_name = 'graphs/north-carolina.html'
    context = {
        'northcarolina': NorthCarolina.objects.all()
    }
    return render(request, 'graphs/north-carolina.html', context)

class NorthDakotaListView(ListView):
    model = NorthDakota
    template_name = 'graphs/north-dakota.html'
    context_object_name = 'northdakota'

def north_dakota(request):
    template_name = 'graphs/north-dakota.html'
    context = {
        'northdakota': NorthDakota.objects.all()
    }
    return render(request, 'graphs/north-dakota.html', context)

class OhioListView(ListView):
    model = Ohio
    template_name = 'graphs/ohio.html'
    context_object_name = 'ohio'

def ohio(request):
    template_name = 'graphs/ohio.html'
    context = {
        'ohio': Ohio.objects.all()
    }
    return render(request, 'graphs/ohio.html', context)

class OklahomaListView(ListView):
    model = Oklahoma
    template_name = 'graphs/oklahoma.html'
    context_object_name = 'oklahoma'

def oklahoma(request):
    template_name = 'graphs/oklahoma.html'
    context = {
        'oklahoma': Oklahoma.objects.all()
    }
    return render(request, 'graphs/oklahoma.html', context)

class OregonListView(ListView):
    model = Oregon
    template_name = 'graphs/oregon.html'
    context_object_name = 'oregon'

def oregon(request):
    template_name = 'graphs/oregon.html'
    context = {
        'oregon': Oregon.objects.all()
    }
    return render(request, 'graphs/oregon.html', context)

class PennsylvaniaListView(ListView):
    model = Pennsylvania
    template_name = 'graphs/pennsylvania.html'
    context_object_name = 'pennsylvania'

def pennsylvania(request):
    template_name = 'graphs/pennsylvania.html'
    context = {
        'pennsylvania': Pennsylvania.objects.all()
    }
    return render(request, 'graphs/pennsylvania.html', context)

class RhodeIslandListView(ListView):
    model = RhodeIsland
    template_name = 'graphs/rhode-island.html'
    context_object_name = 'rhodeisland'

def rhode_island(request):
    template_name = 'graphs/rhode-island.html'
    context = {
        'rhodeisland': RhodeIsland.objects.all()
    }
    return render(request, 'graphs/rhode-island.html', context)

class SouthCarolinaListView(ListView):
    model = SouthCarolina
    template_name = 'graphs/south-carolina.html'
    context_object_name = 'southcarolina'

def south_carolina(request):
    template_name = 'graphs/south-carolina.html'
    context = {
        'southcarolina': SouthCarolina.objects.all()
    }
    return render(request, 'graphs/south-carolina.html', context)

class SouthDakotaListView(ListView):
    model = SouthDakota
    template_name = 'graphs/south-dakota.html'
    context_object_name = 'southdakota'

def south_dakota(request):
    template_name = 'graphs/south_dakota.html'
    context = {
        'southdakota': SouthDakota.objects.all()
    }
    return render(request, 'graphs/south-dakota.html', context)

class TennesseeListView(ListView):
    model = Tennessee
    template_name = 'graphs/tennessee.html'
    context_object_name = 'tennessee'

def tennessee(request):
    template_name = 'graphs/tennessee.html'
    context = {
        'tennessee': Tennessee.objects.all()
    }
    return render(request, 'graphs/tennessee.html', context)

class TexasListView(ListView):
    model = Texas
    template_name = 'graphs/texas.html'
    context_object_name = 'texas'

def texas(request):
    template_name = 'graphs/texas.html'
    context = {
        'texas': Texas.objects.all()
    }
    return render(request, 'graphs/texas.html', context)

class UtahListView(ListView):
    model = Utah
    template_name = 'graphs/utah.html'
    context_object_name = 'utah'

def utah(request):
    template_name = 'graphs/utah.html'
    context = {
        'utah': Utah.objects.all()
    }
    return render(request, 'graphs/utah.html', context)

class VermontListView(ListView):
    model = Vermont
    template_name = 'graphs/vermont.html'
    context_object_name = 'vermont'

def vermont(request):
    template_name = 'graphs/vermont.html'
    context = {
        'vermont': Vermont.objects.all()
    }
    return render(request, 'graphs/vermont.html', context)

class VirginiaListView(ListView):
    model = Virginia
    template_name = 'graphs/virginia.html'
    context_object_name = 'virginia'

def virginia(request):
    template_name = 'graphs/virginia.html'
    context = {
        'virginia': Virginia.objects.all()
    }
    return render(request, 'graphs/virginia.html', context)

class WashingtonListView(ListView):
    model = Washington
    template_name = 'graphs/washington.html'
    context_object_name = 'washington'

def washington(request):
    template_name = 'graphs/washington.html'
    context = {
        'washington': Washington.objects.all()
    }
    return render(request, 'graphs/washington.html', context)

class WestVirginiaListView(ListView):
    model = WestVirginia
    template_name = 'graphs/west-virginia.html'
    context_object_name = 'westvirginia'

def west_virginia(request):
    template_name = 'graphs/west-virginia.html'
    context = {
        'westvirginia': WestVirginia.objects.all()
    }
    return render(request, 'graphs/west-virginia.html', context)

class WisconsinListView(ListView):
    model = Wisconsin
    template_name = 'graphs/wisconsin.html'
    context_object_name = 'wisconsin'

def wisconsin(request):
    template_name = 'graphs/wisconsin.html'
    context = {
        'wisconsin': Wisconsin.objects.all()
    }
    return render(request, 'graphs/wisconsin.html', context)

class WyomingListView(ListView):
    model = Wyoming
    template_name = 'graphs/wyoming.html'
    context_object_name = 'wyoming'

def wyoming(request):
    template_name = 'graphs/wyoming.html'
    context = {
        'wyoming': Wyoming.objects.all()
    }
    return render(request, 'graphs/wyoming.html', context)
