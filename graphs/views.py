from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .forms import (
AlForm,
AkForm,
AzForm,
ArForm,
CaForm,
CoForm,
CtForm,
FlForm,
GaForm,
HiForm,
IdForm,
IlForm,
InForm,
IaForm,
KsForm,
KyForm,
LaForm,
MeForm,
MdForm,
MaForm,
MiForm,
MnForm,
MsForm,
MoForm,
MtForm,
NeForm,
NvForm,
NhForm,
NjForm,
NmForm,
NyForm,
NcForm,
NdForm,
OhForm,
OkForm,
OrForm,
PaForm,
RiForm,
ScForm,
SdForm,
TnForm,
TxForm,
UtForm,
VtForm,
VaForm,
WaForm,
WvForm,
WiForm,
WyForm
)
from django.contrib import messages
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

def alcalculate(request):
    if request.method == 'POST':
        form = AlForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {72.3261 * x - 4359.2334}')
            return redirect('graphs-alabama')
    else:
        form = AlForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def akcalculate(request):
    if request.method == 'POST':
        form = AkForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {7.0693 * x - 179.8722}')
            return redirect('graphs-alaska')
    else:
        form = AkForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def azcalculate(request):
    if request.method == 'POST':
        form = AzForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {552.5456 * x - 40310}')
            return redirect('graphs-arizona')
    else:
        form = AzForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def arcalculate(request):
    if request.method == 'POST':
        form = ArForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {32.4029 * x - 1803.5874}')
            return redirect('graphs-arkansas')
    else:
        form = ArForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def cacalculate(request):
    if request.method == 'POST':
        form = CaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {1681.8456 * x - 97680}')
            return redirect('graphs-california')
    else:
        form = CaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def cocalculate(request):
    if request.method == 'POST':
        form = CoForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {114.4650 * x - 4823.6556}')
            return redirect('graphs-colorado')
    else:
        form = CoForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def ctcalculate(request):
    if request.method == 'POST':
        form = CtForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {417.7299 * x - 16990}')
            return redirect('graphs-connecticut')
    else:
        form = CtForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def decalculate(request):
    if request.method == 'POST':
        form = DeForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {105.0485 * x - 5025.3331}')
            return redirect('graphs-delaware')
    else:
        form = DeForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def flcalculate(request):
    if request.method == 'POST':
        form = FlForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {1434.3040 * x - 10700}')
            return redirect('graphs-florida')
    else:
        form = FlForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def gacalculate(request):
    if request.method == 'POST':
        form = GaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {134.4924 * x - 7233.7582}')
            return redirect('graphs-georgia')
    else:
        form = GaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def hicalculate(request):
    if request.method == 'POST':
        form = HiForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {55.9353 * x - 4405.2253}')
            return redirect('graphs-hawaii')
    else:
        form = HiForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def idcalculate(request):
    if request.method == 'POST':
        form = IdForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {27.0460 * x - 1200.8220}')
            return redirect('graphs-idaho')
    else:
        form = IdForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def ilcalculate(request):
    if request.method == 'POST':
        form = IlForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {1685.9513 * x - 61330}')
            return redirect('graphs-illinois')
    else:
        form = IlForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def iacalculate(request):
    if request.method == 'POST':
        form = IaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {92.1682 * x - 3849.5171}')
            return redirect('graphs-iowa')
    else:
        form = IaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def incalculate(request):
    if request.method == 'POST':
        form = InForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {210.0544 * x - 8571.0272}')
            return redirect('graphs-indiana')
    else:
        form = InForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def kscalculate(request):
    if request.method == 'POST':
        form = KsForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {23.0244 * x - 1026.8946}')
            return redirect('graphs-kansas')
    else:
        form = KsForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def kycalculate(request):
    if request.method == 'POST':
        form = KyForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {67.6330 * x - 3302.8391}')
            return redirect('graphs-kentucky')
    else:
        form = KyForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def lacalculate(request):
    if request.method == 'POST':
        form = LaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {135.8464 * x - 9110.6627}')
            return redirect('graphs-louisiana')
    else:
        form = LaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mecalculate(request):
    if request.method == 'POST':
        form = MeForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {33.1832 * x - 1240.5371}')
            return redirect('graphs-maine')
    else:
        form = MeForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mdcalculate(request):
    if request.method == 'POST':
        form = MdForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {312.8652 * x - 15370}')
            return redirect('graphs-maryland')
    else:
        form = MdForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def macalculate(request):
    if request.method == 'POST':
        form = MaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {510.3481 * x - 19110}')
            return redirect('graphs-massachusetts')
    else:
        form = MaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def micalculate(request):
    if request.method == 'POST':
        form = MiForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {426.0481 * x - 13500}')
            return redirect('graphs-michigan')
    else:
        form = MiForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mncalculate(request):
    if request.method == 'POST':
        form = MnForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {172.6972 * x - 6334.2882}')
            return redirect('graphs-minnesota')
    else:
        form = MnForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mscalculate(request):
    if request.method == 'POST':
        form = MsForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {38.7125 * x - 2438.3240}')
            return redirect('graphs-mississippi')
    else:
        form = MsForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mocalculate(request):
    if request.method == 'POST':
        form = MoForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {108.5834 * x - 4683.2575}')
            return redirect('graphs-missouri')
    else:
        form = MoForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def mtcalculate(request):
    if request.method == 'POST':
        form = MtForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {2.2117 * x - 69.9729}')
            return redirect('graphs-montana')
    else:
        form = MtForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def necalculate(request):
    if request.method == 'POST':
        form = NeForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {98.8781 * x - 4463.4137}')
            return redirect('graphs-nebraska')
    else:
        form = NeForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def nvcalculate(request):
    if request.method == 'POST':
        form = NvForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {217.9531 * x - 13850}')
            return redirect('graphs-nevada')
    else:
        form = NvForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def nhcalculate(request):
    if request.method == 'POST':
        form = NhForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {59.9793 * x - 2218.6178}')
            return redirect('graphs-new-hampshire')
    else:
        form = NhForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def njcalculate(request):
    if request.method == 'POST':
        form = NjForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {412.4337 * x - 15980}')
            return redirect('graphs-new-jersey')
    else:
        form = NjForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def nmcalculate(request):
    if request.method == 'POST':
        form = NmForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {41.0094 * x - 2298.2193}')
            return redirect('graphs-new-mexico')
    else:
        form = NmForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def nycalculate(request):
    if request.method == 'POST':
        form = NyForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {4765.4244 * x - 188600}')
            return redirect('graphs-new-york')
    else:
        form = NyForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def nccalculate(request):
    if request.method == 'POST':
        form = NcForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {174.2733 * x - 10100}')
            return redirect('graphs-north-carolina')
    else:
        form = NcForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def ndcalculate(request):
    if request.method == 'POST':
        form = NdForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {31.2907 * x - 936.0486}')
            return redirect('graphs-north-dakota')
    else:
        form = NdForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def ohcalculate(request):
    if request.method == 'POST':
        form = OhForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {146.9430 * x - 6367.5828}')
            return redirect('graphs-ohio')
    else:
        form = OhForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def okcalculate(request):
    if request.method == 'POST':
        form = OkForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {36.6413 * x - 1921.0990}')
            return redirect('graphs-oklahoma')
    else:
        form = OkForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def orcalculate(request):
    if request.method == 'POST':
        form = OrForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {45.0619 * x - 2162.8279}')
            return redirect('graphs-oregon')
    else:
        form = OrForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def pacalculate(request):
    if request.method == 'POST':
        form = PaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {574.7566 * x - 2.568e+04}')
            return redirect('graphs-pennsylvania')
    else:
        form = PaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def ricalculate(request):
    if request.method == 'POST':
        form = RiForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {279.2690 * x - 12890}')
            return redirect('graphs-rhode-island')
    else:
        form = RiForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def sccalculate(request):
    if request.method == 'POST':
        form = ScForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {75.1662 * x - 4418.8077}')
            return redirect('graphs-south-carolina')
    else:
        form = ScForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def sdcalculate(request):
    if request.method == 'POST':
        form = SdForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {59.2707 * x - 1831.7510}')
            return redirect('graphs-south-dakota')
    else:
        form = SdForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def tncalculate(request):
    if request.method == 'POST':
        form = TnForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {167.2234 * x - 9287.2448}')
            return redirect('graphs-tennessee')
    else:
        form = TnForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def txcalculate(request):
    if request.method == 'POST':
        form = TxForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {528.5798 * x - 35280}')
            return redirect('graphs-texas')
    else:
        form = TxForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def utcalculate(request):
    if request.method == 'POST':
        form = UtForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {148.8861 * x - 6724.3751}')
            return redirect('graphs-utah')
    else:
        form = UtForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def vtcalculate(request):
    if request.method == 'POST':
        form = VtForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {9.7194 * x - 264.7687}')
            return redirect('graphs-vermont')
    else:
        form = VtForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def vacalculate(request):
    if request.method == 'POST':
        form = VaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {304.0044 * x - 15550}')
            return redirect('graphs-virginia')
    else:
        form = VaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def wacalculate(request):
    if request.method == 'POST':
        form = WaForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {305.9589 * x - 13660}')
            return redirect('graphs-washington')
    else:
        form = WaForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def wvcalculate(request):
    if request.method == 'POST':
        form = WvForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {5.3579 * x - 240.0965}')
            return redirect('graphs-west-virginia')
    else:
        form = WvForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def wicalculate(request):
    if request.method == 'POST':
        form = WiForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {181.1103 * x - 6667.8346}')
            return redirect('graphs-wisconsin')
    else:
        form = WiForm()
    return render(request, 'graphs/alpredict.html', {'form': form})

def wycalculate(request):
    if request.method == 'POST':
        form = WyForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            messages.success(request, f'The predicted number of cases will be about {3.7826 * x - 118.9053}')
            return redirect('graphs-wyoming')
    else:
        form = WyForm()
    return render(request, 'graphs/alpredict.html', {'form': form})


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
