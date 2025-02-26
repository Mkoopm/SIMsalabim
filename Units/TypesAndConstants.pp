unit TypesAndConstants;
{provides the types and constants used by SIMsalabim}

{
SIMsalabim: a 1D drift-diffusion simulator 
Copyright (c) 2020 Dr T.S. Sherkar, V.M. Le Corre, M. Koopmans,
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
email: l.j.a.koster@rug.nl
surface mail: 
L.J.A. Koster
Zernike Institute for Advanced Materials
Nijenborgh 4, 9747 AG Groningen, the Netherlands
}

{$MODE OBJFPC} {force OBJFPC mode}

interface

const
    Max_NP = 2000;     {max number of grid points except contacts}

type myReal = EXTENDED; 
	 vector = ARRAY[0..Max_NP + 1] OF myReal;
     ShortIntVector = ARRAY[0..Max_NP + 1] OF ShortInt;
     Row = ARRAY OF myReal; 
     Table = ARRAY OF ARRAY OF myReal; {used to store mob_tab, table with elec. mob. as a function of F and n}
     MathFunc = FUNCTION(x : myReal) : myReal;
     MathFuncValues = FUNCTION(x : myReal; vals : Row) : myReal;

implementation

begin 

end.
