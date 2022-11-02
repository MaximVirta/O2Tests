import JPyPlotRatio
import ROOT

msize = 5.0

data_plotParam = [
  {'plotType':'data','color':'k','fmt':'s',"mfc":"none",'markersize':msize}
];

obs = ["hJetPt", "hJetEta"];

fin = ROOT.TFile("AnalysisResults.root", "READ")

ylabels = ["$1/N_{evt}\\, dN/dp_T$","$dN/d\\eta$"]
xlabels = ["$p_T$ (GeV/c)", "$\\eta$"]

tdir = fin.Get("twoparcorcombexample")

Nevt = tdir.Get("hZvertex").GetEntries();

for i,s in enumerate(obs):
	plot = JPyPlotRatio.JPyPlotRatio(panels=(1,1), panelSize=(4,5),
									disableRatio=[0], ylabel=ylabels[i], xlabel=xlabels[i],
									legendPanel={0:0}, legendLoc={0:(0.5,0.6)})

	if (i==0): 
		plot.GetAxes(0).set_yscale("log")
		for k,a in enumerate(plot.ax[:,0]):
			a.set_yscale("log");
			a.set_yticks([(10**i) for i in range(-5,0)]);
	
	plot.EnableLatex(True)
	gr = tdir.Get(s);
	gr.Scale(1./Nevt,"width")
	plot.Add(0, gr, **data_plotParam[0]);

	plot.Plot()
	plot.Save("/home/maxim/o2tests/figs/plot_%s.pdf" % s)