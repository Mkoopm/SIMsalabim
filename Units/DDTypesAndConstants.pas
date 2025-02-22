unit DDTypesAndConstants;
{provides drift-diffusion-specific types and constants}

{
SIMsalabim:a 1D drift-diffusion simulator 
Copyright (c) 2021 Dr T.S. Sherkar, Dr V.M. Le Corre, M. Koopmans,
F. Wobben, and Prof. Dr. L.J.A. Koster, University of Groningen
This source file is part of the SIMsalabim project.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License and 
the GNU Lesser General Public License along with this program.


The SIMsalabim project can be found on Github at https://github.com/kostergroup/SIMsalabim 
email:l.j.a.koster@rug.nl
surface mail: 
L.J.A. Koster
Zernike Institute for Advanced Materials
Nijenborgh 4, 9747 AG Groningen, the Netherlands
}

{$MODE OBJFPC} {force OBJFPC mode}

INTERFACE

USES TypesAndConstants; {provides a couple of types}

CONST
    DDTypesAndConstantsVersion = '4.25'; {version of this unit}
    parameter_file = 'device_parameters.txt'; {name of file with parameters}
    q = 1.6022e-19;  	{C} {elementary charge}
    k = 1.3807e-23;     {J/K} {Boltzmann's constant}
    eps_0 = 8.8542e-12; {F/m} {dielectric constant of vacuum}
    maxGenProfPoints = 5000; {max number of grid points in generation profile}
    maxExpData = 10000; {max number of experimental JV points}
	minExpData = 4;     {min number of experimental JV points}
	tolReal = 1e-6;     {tolerance: when are 2 floats equal?}

{Magic numbers, used in the code:}
    {Name                    Where                        What does it do?}
    threshold_err = 0.1; {IN: Find_Solar_Cell_Parameters, defines max relative error when displaying solar cell parameters}
    MaxInterpolationOrder = 3; {IN: Find_Solar_Cell_Parameters, maximum interpolation order in estimating Jsc, Voc}
    temp_file = '.temp.txt';{IN: Tidy_up_parameter_file_Exit, a temporary file used to store the device parameters}
    myDelims = [#0..' ', ';', '/', '\', '''', '"', '`', '*', '=']; {IN Tidy_up_parameter_file_Exit, note: not a decimal point or comma!}
    nd = 20; {IN: main, it limits the number of digits to this value to prevent unnecessarily large output files}
    minErr = 1E-4; {IN: Calc_and_Output_Soalr_Cell_Parameters, lower bound to error in parameters}
    tab1 = 6; {IN: Calc_and_Output_Solar_Cell_Parameters, 1st position of tab in table with solar cell parameters}
    tab2 = 28; {IN: Calc_and_Output_Solar_Cell_Parameters, 2nd position of tab in table with solar cell parameters}
    tab3 = 50; {IN: Calc_and_Output_Solar_Cell_Parameters, 3rd position of tab in table with solar cell parameters}
	MinCountStatic = 5; {number of time steps we consider to be static}
	MinCountChangeSmall = 3; {IN: determine_convergence, used if loop hardly changes.}
	MinCountJSmall = 3; {IN: determine_convergence, used if we're simulating really small currents.}
    
TYPE 
    TProgram = (ZimT, SimSS); {which program are we using?}
    
    TJVList = ARRAY OF RECORD {for storing the JV curve}
                        Vint, Vext : myReal;
                        Jint, Jext : myReal;
                        UpdateIons, Store, Use : BOOLEAN
                      END;

    TRec = RECORD {for storing the linearization of f_ti and f_tb at a grid point}
                        direct, bulk, int, {direct (band to band), bulk SRH, interface SRH recombination respectively}
                        {the rest are auxiliary variables:}
                        old_Rint, m_srhi, lo_srhi, up_srhi, rhs_srhi,
						dir_cont_rhs, dir_cont_m, bulk_cont_rhs, bulk_cont_m,
						int_cont_lo, int_cont_up, int_cont_m, int_cont_rhs : vector;        
            END;	

	TState = RECORD {stores all variables that either define a state or change in time}
				    Gehp, tijd : myReal; {set by input}
				    dti, Vint, Vext, Jint, Jext : myReal; {derivative variables or result of simulation}
				    SimType, convIndex : INTEGER; 
				    V, Vgn, Vgp, n, p, nion, pion, Gm, 
				    Jn, Jp, Jnion, Jpion, JD, mun, mup,
				    gen, Lang, SRH, diss_prob, 
				    Ntb_charge, Nti_charge, {charge density of bulk/interface trap}
				    f_tb, f_ti : vector; {f_tb/i: occupancy of bulk/interface trap}
				    Rn, Rp : TRec;
			  END;

    Tfitmode = (linear, logarithmic);

	
	TStaticVars = RECORD {stores all parameters that are calculated from input, but don't change during the simulation}
					NcLoc, ni, eps, h, x, nid, pid, E_CB, E_VB, nt0, pt0, Ntb, Nti, orgGm : vector;
					Egap, epsi, phi_left, phi_right, V0, VL, Vt, Vti					  : myReal;
					i1, i2, cwe_b, NJV													  : INTEGER;
					cwe_i, q_tr_igb														  : vector;
					Traps, Traps_int, Traps_int_poisson									  : BOOLEAN;
				  END;

	TInputParameters =  RECORD {all input parameters and ones that are directly derived from the input (e.g. booleans)}
							{order of variables: same as in input file, but grouped by type}
							{Floating point:}
							T, L, eps_r, CB, VB, Nc, n_0, p_0, mun_0, 
							mup_0, gamma_n, gamma_p,
							W_L, W_R,
							Sn_R, Sn_L, Sp_L, Sp_R, Rseries, Rshunt, L_LTL, L_RTL, Nc_LTL, 
							Nc_RTL, doping_LTL, doping_RTL, mob_LTL, mob_RTL,  
							nu_int_LTL, nu_int_RTL, eps_r_LTL, eps_r_RTL, 
							CB_LTL, VB_LTL, CB_RTL, VB_RTL, CNI, CPI,
							mobnion, mobpion,
							Gehp, Gfrac, P0, a, 
							kf, Lang_pre, kdirect,
							Bulk_tr, St_L, St_r, GB_tr, 
							Cn, Cp, Etrap, tolPois, maxDelV,
							tolJ, MinRelChange, accDens, grad, TolRomb, 
							LowerLimBraun, UpperLimBraun,
							TolVint,
							MinAbsJDark, Vpre, Vmin, Vmax, Vstep, Vacc, rms_threshold : myReal; 
							{integers:}		
							MaxItPois, MaxRombIt, 
							mob_n_dep, mob_p_dep,
							ThermLengDist, ion_red_rate, num_GBs, Tr_type_L, Tr_type_R, Tr_type_B, 
							NP, CurrDiffInt, MaxItSS, MaxItTrans, 
							FailureMode, OutputRatio, Vdistribution, Vscan, 
							Pause_at_end : INTEGER; 
							{derived booleans:}
							Field_dep_G, negIonsMove, posIonsMove, TLsAbsorb,
							IonsInTLs, TLsTrap, Use_gen_profile, UseLangevin, 
							IgnoreNegDens, AutoTidy, StoreVarFile, 
							PreCond, until_Voc, UseExpData, AutoStop : BOOLEAN;
							{filenames and other strings:}
							Gen_profile, log_file, tVG_file, Var_file, tj_file, ExpJV, JV_file, scPars_file : ANSISTRING;
							{Misc:}
							rms_mode : Tfitmode;	
						END;
	
	TSCPar = RECORD {for storing solar cell parameters}
				Jsc, Vmpp, MPP, FF, Voc, ErrJsc, ErrVmpp, ErrMPP, ErrFF, ErrVoc : myReal;
				calcSC, calcMPP, calcFF, calcOC : BOOLEAN
			  END;

    TLinFt = RECORD {for storing the linearization of f_ti and f_tb at a grid point}
                        f_ti_lo, f_ti_up, f_ti_m, f_ti_rhs : vector;
                        f_tb_m, f_tb_rhs : vector;
             END;							
											
	TItResult = ARRAY OF RECORD {we use this in MainSolver to store the J, change and error estimate in every iteration loop}
						Jint, RangeJ, relchange, error : myReal;
						CountChangeSmall, CountJSmall : INTEGER;
					END;									
		

IMPLEMENTATION

BEGIN 

END.
