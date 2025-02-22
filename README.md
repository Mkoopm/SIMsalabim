# SIMsalabim Project

SIMsalabim: A 1D drift-diffusion simulator for semiconductor devices (LEDs, solar cells, diodes, organics, perovskites). It consists of two programs that share most of their code: SimSS (simulates steady-state), and ZimT (zimulates transients).

## Table of Contents
1. [Introduction](#introduction)
2. [Quickstart guide](#quickstart-guide)
3. [Instructional videos](#instructional-videos)
4. [Running SIMsalabim](#running-simss-or-zimt)
5. [How to cite](#how-to-cite)
6. [Copyright and license](#copyright-and-license)
7. [How to contribute](#how-to-contribute)
8. [Scientific publications based on SIMsalabim](#scientific-publications-based-on-the-simsalabim-project)

## Introduction

SimSS and ZimT can be used to simulate current-voltage (JV) characteristics of semiconductor devices. This includes the effects of generation, recombination and trapping of electrons and holes, the effect of ions and dopants, and self-consistently solves the electric field that results from all charged species. It is up to the user to make sure that the physical model that underlies SIMsalabim is applicable (see Reference Manual for more details).

The routines that make up this project are used in two different guises: SimSS and ZimT. The former is a steady-state version and is the 'main' code. The latter, ZimT, can be used to simulate transients. 
The project folder is structured as follows:
- Docs: this folder contains a reference manual, developer guidelines, and a log of all changes to the code
- SimSS: contains the steady-state version of this software
- Tests: contains a number of tests to assess the functioning of the codes (SimSS and ZimT)
- Units: this is where the heart of the code resides. These units are shared between SimSS and ZimT
- ZimT: the transient equivalent of SimSS


## Quickstart guide
There are two ways to get SimSS or ZimT running on your machine:
1. [Use pre compiled binaries](#Pre-compiled-binaries)
2. [Compile SIMsalabim](#Compiling-SIMsalabim)

While using the pre-compiled binaries is easiest, they will not work on every machine. If they do not work follow the instructions for compiling SIMsalabim.

### Pre-compiled binaries

SimSS and ZimT come as pre-compiled binaries for WIN or Linux (64 bits), see [releases](https://github.com/kostergroup/SIMsalabim/releases). This avoids having to download and install the FPC compiler and compiling the code which is described below. There is no guarantee that these will work, but it is worth a try. Simply copy the binary to the main SimSS/ZimT folder. The Linux one might require a change of permissions to run, something like:
<pre><code>
    chmod +x simss
 </code></pre>

### Compiling SIMsalabim

There are 3 steps to complete to run SimSS or ZimT for the first time:
  1. Install the "Free Pascal" compiler.
  2. Compile SimSS (or ZimT).
  3. Run SimSS (or ZimT). 

SimSS and ZimT should compile and run on any platform supported by the "Free Pascal" compiler. We provide detailed instructions for installing both the compiler and running the code for Windows and Linux (Ubuntu). For any other platform, please install the compiler (version 3.2.0 or newer) following the instructions from https://www.freepascal.org/. Steps 2 and 3 (compile and run) should be similar to the Ubuntu and Windows steps outlined below.

Below are the instructions for performing these steps on Ubuntu (or any other Debian based Linux distribution) and Windows.  


### Ubuntu (Linux) guide

Navigate to the SimSS or ZimT folder, where you can find simss.pas or zimt.pas. This example assumes you want to compile SimSS, but you can replace `simss` with `zimt` in the commands and run from the ZimT folder to compile and run ZimT. 

**Ubuntu 20.10 or newer:**
Steps:
  - Open a terminal in the SimSS folder
  - run the following commands to perform step 1, 2, and 3 (install, compile, run):
```
sudo apt install fpc
fpc simss
./simss
```

**Ubuntu 20.04 or older:**
We need a relatively recent version of the Pascal compiler (v 3.2.0 or higher). Therefore, manual installation of the compiler is required on Ubuntu 20.04 or older.
Steps:
  - Download the relevant version of the compiler from https://www.freepascal.org/
  - Install the compiler. This is done by running the installation script that can be found in the downloaded archive. While it can be installed without root privilege, the compiler should be manually added to path making installation a bit more tricky. To install as root run the command: `sudo ./install.sh`. 
  - Open a terminal in the SimSS folder
  - run the following commands to perform step 2 and 3 (compile and run):
```
fpc simss
./simss
```

**Installing on other Linux distributions:**
Most package managers for other Linux distributions ship the compiler package in a recent enough version (version 3.2.0 or newer of package *fpc*), so it suffices to exchange the *apt install* command with another package manager's equivalent. 

### Windows guide

Navigate to the SimSS or ZimT folder, where you can find simss.pas or zimt.pas. This example assumes you want to compile SimSS, but you can replace `simss` with `zimt` in the commands and run from the ZimT folder to compile and run ZimT. 

Steps:
  - Download and install fpc from https://www.freepascal.org/ (SimSS and ZimT require version 3.2.0 or newer)
  - Open a command prompt or powershell instance in the SimSS folder (for example by opening the folder in explorer, pressing <kbd>alt</kbd>+<kbd>D</kbd> to select the location bar, typing 'cmd' and pressing <kbd>enter</kbd>).
  - run the following commands to perform step 2 and 3 (compile, run):
  
```
fpc simss
simss.exe
```

Alternative:
  - Install Windows subsystem for Linux.
  - Follow the Ubuntu instructions above.


### Miscellaneous

**Warning message**
You may see this warning message when compiling the codes:
/usr/bin/ld.bfd: warning: link.res contains output sections; did you forget -T?
Just ignore this.

**Editing the code**
You'll probably want to use (install?) some form of integrated development environment (IDE). Most modern IDE's include syntax highlighting for the Pascal language. Popular IDEs include Lazarus, Geany, and Visual studio code (requires extension to perform syntax highlighting for pascal). Some guidelines for extending the code can be found in Docs/Developer_guidelines.md.


## Instructional videos

In order to help new users to get the most out of SimSS/ZimT, we have recorded a few instructional videos: 

1 [Installation and basic use](https://youtu.be/0mtpGJMnbFE "Installation and basic use")

Please note that at the time of recording SimSS was called SIMsalabim, so the project name and the name of one of the programs was the same.


## Running SimSS or ZimT
- all parameters are specified in device_parameters.txt (in ZimT an additional time-voltage-generation (tVG) file is present to indicate what time, generation, and voltage at every simulation step).
- on Linux run SimSS/ZimT by entering in the terminal from the folder where the compiled program is located and run using
<pre><code>
./simss
</code></pre>
or 
<pre><code>
./zimt
</code></pre>
on windows:
<pre><code>
simss.exe
</code></pre>
or 
<pre><code>
zimt.exe
</code></pre>
Alternatively, the programs can be double clicked in the file manager on both Windows and Linux to run.

- all parameters listed in device_parameters.txt can also be changed via the command line. This will override the respective parameter value in device_parameters.txt. Simply add the parameter name and value to the command line after a dash (-).
Example: change of thickness (L) and JV output file (JV_file):
<pre><code>
./simss -L 345E-9 -JV_file anotherJV.dat
</code></pre>
- multiple output files will be generated (see device_parameters) and log file.

4) Other remarks
- in general, input files and the log file have extension .txt, whereas output files that can be used for plotting (J-V curves, for example) have extension .dat.
- all changes are shown and commented on in the file Docs/Change_log.txt. Here we document not just the changes, but also explain and motivate some of the choices in naming, physical models, etc. 


## How to cite

The essentials of this code have been outlined in several publications. 
The original paper showing how this code can be used for organic solar cells is: 
- L.J.A. Koster, E. C. P. Smits, V. D. Mihailetchi, and P. W. M. Blom, Device model for the operation of polymer/fullerene bulk heterojunction solar cells, Phys. Rev. B **72**, 085205 (2005).

For the use of perovskite solar cells, the following paper offers a detailed description of the modelling assumptions:
- T.S. Sherkar, C. Momblona, L. Gil-Escrig, J. Ávila, M. Sessolo, H. Bolink, and L.J.A. Koster, Recombination in Perovskite Solar Cells: Significance of Grain Boundaries, Interface Traps and Defect Ions, ACS Energy Lett. **2**, 1214 (2017).


## Copyright and license

The SIMsalabim project is licensed under the GNU Lesser General Public Licence version 3. The details of this licence can be found in the files COPYING.txt and COPYING.LESSER.txt. 
Several authors (all from the University of Groningen) have contributed to the code: 
- Dr T.S. (Tejas) Sherkar
- Dr V.M. (Vincent) Le Corre
- M. (Marten) Koopmans
- F. (Friso) Wobben
- Prof. Dr. L.J.A. (Jan Anton) Koster


## How to contribute
If you would like to would like to contribute to the SIMsalabim project or have any questions, please read the [Developer instructions](https://github.com/kostergroup/SIMsalabim/blob/master/Docs/Developer_guidelines.md). It covers how we would like to approach both questions and possible code changes.


## Scientific publications based on the SIMsalabim project

List of publications (not complete):

- V.M. Le Corre, T.S. Sherkar, M. Koopmans, and L.J.A. Koster, Identification of the Dominant Recombination Process for Perovskite Solar Cells Based on Machine Learning, Cell Rep. Phys. Sci. 2, 100346 (2021).

- Y. Firdaus, V.M. Le Corre, S. Karuthedath, W. Liu, A. Markina, W. Huang, S. Chattopadhyay, M.M. Nahid, M.I. Nugraha, A. Seitkhan, A. Basu, Y. Lin, I. McCulloch, H. Ade, J. Labram, F. Laquai, D. Andrienko, L.J.A. Koster, and T.D. Anthopoulos, Long-range exciton diffusion in molecular non-fullerene acceptors, Nature Comm. 11, 5220 (2020).

- D. Hu, Q. Yang, H. Chen, F. Wobben, V.M. Le Corre, R. Singh, L.J.A. Koster, Z. Kan, Z. Xiao, and S. Lu, 15.34% Efficiency All-Small-Molecule Organic Solar Cells with Improved Fill Factor Enabled by a Fullerene Additive, Energy Environ. Sci. 13, 2134 (2020).

- L. Hou, J. Lv, F. Wobben, V.M. Le Corre, H. Tang, R. Singh, M. Kim, F. Wang, H. Sun, W. Chen, Z. Xiao, M. Kumar, T. Xu, W. Zhang, I. McCulloch, T. Duan, H. Xie, L.J.A. Koster, S. Lu, and Z. Kan, Effects of Fluorination on Fused Ring Electron Acceptor for Active Layer Morphology, Exciton Dissociation, and Charge Recombination in Organic Solar Cells, ACS Appl. Mater. Interfaces 12, 56231 (2020).

- E.A. Duijnstee, V.M. Le Corre, M.B. Johnston, L.J.A. Koster, J. Lim, and H.J. Snaith, Understanding dark current-voltage characteristics in metal-halide perovskite single crystals, Phys. Rev. Appl. 15, 014006 (2021).

- D. Neher, J. Kniepert , A. Elimelech, and L.J.A. Koster, A new Figure of Merit for Organic Solar Cells with Transport-limited Photocurrents, Sci. Rep. 6, 24861 (2016).

- S. Shao, M. Abdu-Aguye, T.S. Sherkar, H.-H. Fang, G. ten Brink, B.J. Kooi, L.J.A. Koster, and M.A. Loi, The effect of the microstructure on trap-assisted recombination and light soaking phenomenon in hybrid perovskite solar cells, Adv. Funct. Mater. 26, 8094 (2016).

- T.S. Sherkar, C. Momblona, L. Gil-Escrig, H.J. Bolink, and L.J.A. Koster, Improving perovskite solar cells: Insights from a validated device model, Adv. Energy Mater. 1602432 (2017).
 
- T.S. Sherkar, C. Momblona, L. Gil-Escrig, J. Ávila, M. Sessolo, H. Bolink, and L.J.A. Koster, Recombination in Perovskite Solar Cells: Significance of Grain Boundaries, Interface Traps and Defect Ions, ACS Energy Lett. 2, 1214 (2017).

- V.M. Le Corre, A. Rahimi Chatri, N.Y. Doumon, and L.J.A. Koster, Charge carrier extraction in organic solar cells governed by steady-state mobilities, Adv. Energy Mater. 1701138 (2017).

- F.J.M. Colberts, M.M. Wienk, R. Heuvel, W. Li, V.M. Le Corre, L.J.A. Koster, and R.A.J. Janssen, Bilayer-Ternary Polymer Solar Cells Fabricated Using Spontaneous Spreading on Water, Adv. Energy Mater. 8, 1802197 (2018).

- N.Y. Doumon, M.V. Dryzhov, F.V. Houard, V.M. Le Corre, A. Rahimi Chatri, P. Christodoulis, and L.J.A. Koster, Photostability of Fullerene and Non-Fullerene Polymer Solar Cells: The Role of the Acceptor, ACS Appl. Mater. Interfaces 11, 8310 (2019).

- V.M. Le Corre,  M. Stolterfoht, L. Perdigón Toro, M. Feuerstein, C. Wolff, L. Gil-Escrig, H.J. Bolink, D. Neher, and L.J.A. Koster, Charge transport layers limiting the efficiency of perovskite solar cells: how to optimize conductivity, doping and thickness, ACS Appl. Energy Mater. 2, 6280 (2019). 

- E. A. Duijnstee, J.M. Ball, V.M. Le Corre, L.J.A. Koster, H.J. Snaith, and J. Lim, Towards Understanding Space-charge Limited Current Measurements on Metal Halide Perovskites, ACS Energy Lett. 5, 376 (2020).

- D. Bartesaghi and L. J. A. Koster, The effect of large compositional inhomogeneities on the performance of organic solar cells: A numerical study, Adv. Funct. Mater. 25, 2013 (2015).

- J. Kniepert, I. Lange, J. Heidbrink, J. Kurpiers, T. Brenner, L.J.A. Koster, and D. Neher, Effect of Solvent Additive on Generation, Recombination and Extraction in PTB7:PCBM Solar Cells: A conclusive Experimental and Numerical Simulation Study, J. Phys. Chem. C 119, 8310 (2015).

- D. Bartesaghi, I. del Carmen Pérez, J. Kniepert, S. Roland, M. Turbiez, D. Neher, and L.J.A. Koster, Competition between recombination and extraction of free carriers determines the fill-factor of organic solar cells, Nature Comm. 6, 7083 (2015).

- N.J. van der Kaap, I. Katsouras, K. Asadi, P.W.M. Blom, L.J.A. Koster, and D.M. de Leeuw, Charge transport in disordered semiconducting polymers driven by nuclear tunneling, Phys. Rev. B 93, 140206(R) (2016).

- D. Bartesaghi, M. Turbiez, and L. J. A. Koster, Charge Transport and Recombination in PDPP5T:[70]PCBM Organic Solar Cells: the Influence of Morphology, Org. Elec. 15, 3191 (2014).

- G. A. H. Wetzelaer, N. J. van der Kaap, L. J. A. Koster, and P. W. M. Blom, Quantifying bimolecular recombination in organic solar cells in steady-state, Adv. Energy Mater. 3, 1130 (2013).

- J. Kniepert, I. Lange, N. J. van der Kaap, L. J. A. Koster, and D. Neher, A conclusive view on charge generation, recombination and extraction in as-prepared and annealed P3HT:PCBM blends: a combined experimental-simulation work, Adv. Energy Mater. 4, 1301401 (2014).

- L. J. A. Koster, M. Kemerink, M. M. Wienk, K. Maturová, and R. A. J. Janssen, Quantifying bimolecular recombination losses in bulk heterojunction solar cells, Adv. Mater. 63, 1670 (2011).

- G. A. H. Wetzelaer, L. J. A. Koster, and P. W. M. Blom, Validity of the Einstein relation in disordered organic semiconductors, Phys. Rev. Lett. 107, 066605 (2011).

- L.J.A. Koster, S. E. Shaheen, and J. C. Hummelen, Pathways to a new efficiency regime for organic solar cells, Adv. Energy Mater. 2, 1246 (2012). Listed in Adv. Energy Mater. top-5 most accessed articles in May 2012
- D.J. Wehenkel, L.J.A. Koster, M. M. Wienk, and R. A. J. Janssen, Influence of injected charge carriers on photocurrents in polymer solar cells, Phys. Rev. B 85, 125203 (2012).
- M. Kuik, L. J. A. Koster, A. G. Dijkstra, G. A. H. Wetzelaer, and P. W. M. Blom, Non-radiative recombination losses in polymer light-emitting diodes, Org. Elec. 13, 969 (2012).

- M. Kuik, L. J. A. Koster, G. A. H. Wetzelaer, and P. W. M. Blom, Trap-assisted recombination in disordered organic semiconductors, Phys. Rev. Lett. 107, 256805 (2011).

- L. J. A. Koster, Charge carrier mobility in disordered organic blends for photovoltaics, Phys. Rev. B 81, 205318 (2010).

- M. M. Mandoc, W. Veurman, L. J. A. Koster, M. M. Koetse, J. Sweelssen, B. de Boer, and P. W. M. Blom, Charge transport in MDMO-PPV : PCNEPV all-polymer solar cells, J. Appl. Phys. 101, 104512 (2007).

- V. D. Mihailetchi, H. Xie, B. de Boer, L. J. A. Koster, and P. W. M. Blom, Charge Transport and Photocurrent Generation in Poly(3-hexylthiophene):Methanofullerene Bulk-Heterojunction Solar Cells, Adv. Funct. Mater. 16, 699 (2006).L. J. A. Koster, W. J. van Strien, W. J. E. Beek, and P. W. M. Blom, Device operation of conjugated polymer/zinc oxide bulk heterojunction solar cells, Adv. Funct. Mater. 17, 1297 (2007). 

- M. M. Mandoc, L. J. A. Koster, and P. W. M. Blom, Optimum charge carrier mobility in organic solar cells, Appl. Phys. Lett. 90, 133504 (2007).

- M. M. Mandoc, W. Veurman, L. J. A. Koster, B. de Boer, and P. W. M. Blom, Origin of the Reduced Fill Factor and Photocurrent in MDMO-PPV:PCNEPV All-Polymer Solar Cells, Adv. Funct. Mater. 17, 2167 (2007).J. D. Kotlarski, M. Lenes, L. J. A. Koster, L. H. Slooff, and P. W. M. Blom, Combined optical and electrical modeling of polymer:fullerene bulk heterojunction solar cells, J. Appl. Phys. 103, 084502 (2008).

- L. J. A. Koster, V. D. Mihailetchi, and P. W. M. Blom, Ultimate efficiency of polymer/fullerene bulk heterojunction solar cells, Appl. Phys. Lett. 88, 093511 (2006).

- M. Lenes, L. J. A. Koster, V. D. Mihailetchi, and P. W. M. Blom, Thickness dependence of the efficiency of polymer:fullerene bulk heterojunction solar cells, Appl. Phys. Lett. 88, 243502 (2006).

- L. J. A. Koster, V. D. Mihailetchi, and P. W. M. Blom, Bimolecular recombination in polymer/fullerene bulk heterojunction solar cells, Appl. Phys. Lett. 88, 052104 (2006).
 
- V. D. Mihailetchi, H. Xie, B. de Boer, L. J. A. Koster, L. M. Popescu, J. C. Hummelen, and P. W. M. Blom, Origin of the enhanced performance in poly(3-exylthiophene):methanofullerene solar cells using slow drying, Appl. Phys. Lett. 89, 012107 (2006).
  
- L. J. A. Koster, E. C. P. Smits, V. D. Mihailetchi, and P. W. M. Blom, Device model for the operation of polymer/fullerene bulk heterojunction solar cells, Phys. Rev. B 72, 085205 (2005).
  
- L. J. A. Koster, V. D. Mihailetchi, R. Ramaker, and P. W. M. Blom, Light intensity dependence of open-circuit voltage of polymer:fullerene solar cells, Appl. Phys. Lett. 86, 123509 (2005).
   
- L. J. A. Koster, V. D. Mihailetchi, H. Xie, and P. W. M. Blom, Origin of the light intensity dependence of the short-circuit current of polymer/fullerene solar cells, Appl. Phys. Lett. 87, 203502 (2005).






