import JPyPlotRatio
import ROOT

msize = 5.0

data_plotParam = [
  {'plotType':'data','color':'k','fmt':'s',"mfc":"none",'markersize':msize}
];


fin = ROOT.TFile("AnalysisResults.root", "READ")

tdir = fin.Get("twoparcorcombexample")

plot = JPyPlotRatio.JPyPlotRatio(panels=(1,1), panelSize=(4,5),
								disableRatio=[0], ylabel="$dN_{evt}/dz$", xlabel="z (cm)",
								legendPanel={0:0}, legendLoc={0:(0.5,0.6)})

plot.EnableLatex(True)


gr = tdir.Get("hZvertex");
gr.Scale(1.,"width")
plot.Add(0, gr, **data_plotParam[0]);

plot.Plot()
plot.Save("figs/plot_hZvertex.pdf")
