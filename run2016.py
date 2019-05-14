from lsctools import config, prepare, gather, fit, plot, analyze

# Load 2016 configuration
config.PCC2016ReRecoJan2017()

# Find ROOT files belonging to LS scans
prepare.findRootFiles('fulltrees')

for scan in config.options['scans']:
    # Get vertex data from ROOT files
    gather.vertexPositionPerBxStep(scan, all=True, alternative=True)

    # Fit vertex positions at each step with Gaussian
    fit.vertexPosition(scan, all=True, alternative=True, fitmethod='L')
    
    # Create plots of vertex distribution at each step
    plot.vertexPositionPerBxStep(scan, all=True, alternative=True, fit='L')

    # Analyze full scan
    analyze.vertexPosition(scan, all=True, alternative=True, fitted='L')

    # Plot full scan results
    plot.vertexPositionPerDirectionBx(scan, all=True, alternative=True, fitted='L')
