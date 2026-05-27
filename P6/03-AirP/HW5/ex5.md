1- There is an airplan with the following properties:

\begin{itemize}
    \item $V$ : airspeed (mile/hr)
    \item $v$ : airspeed (ft/sec)
    \item $\rho_0 = 0.0024 \text{ slugs/ft}^3$ : air density at sea level
    \item $\rho_{36000} = 0.00072 \text{ slugs/ft}^3$ : air density at $36,000 \text{ ft}$
    \item $c = 0.8 \text{ lbs/(lb}\cdot\text{hr)}$ : specific fuel consumption (SFC)
    \item $w_1$ : final weight
    \item $w_0$ : initial weight
    \item $R$ : range (mile) $= \frac{V}{c} \left(\frac{L}{D}\right) \ln\left(\frac{w_0}{w_1}\right) = 2.3 \frac{V}{c} \left(\frac{L}{D}\right) \log_{10}\left(\frac{w_0}{w_1}\right)$
    \item $S = 3000 \text{ ft}^2$ : wing planform area
    \item $S_t = 900 \text{ ft}^2$ : tail planform area
    \item $b = 150 \text{ ft}$ : wingspan
    \item $l = 150 \text{ ft}$ : aircraft length
    \item $d_f = 12 \text{ ft}$ : fuselage diameter
    \item $d_e = 5 \text{ ft}$ : engine diameter
    \item $h$ : altitude in $\text{ft}$
    \item $C''$ : fuel consumption rate ($\text{lb/mile}$)
    \item $a$ : acceleration
    \item $G$ : glide distance
    \item $f = 0.02$ : rolling friction coefficient
    \item $f_b$ : braking friction coefficient
    \item $w_g = 330000 \text{ lbs}$ : gross takeoff weight (GTOW)
    \item $w_e = 150000 \text{ lbs}$ : operating empty weight (OEW)
    \item $w_f = 150000 \text{ lbs}$ : maximum fuel weight
    \item $w_r = 15000 \text{ lbs}$ : reserve fuel weight
    \item $w_p = 100000 \text{ lbs}$ : payload weight ($w_g - w_e - w_f$)
    \item $n = 4$ : number of engines
    \item $T_0 = 4 \times 15000 \text{ lbs}$ : total thrust at sea level
    \item $T_{36000} = 4 \times 4000 \text{ lbs}$ : total thrust at $36,000 \text{ ft}$ altitude
    \item $C_{L_{max}} = 1.5$ : maximum lift coefficient (for landing and takeoff)
    \item $C_D = C_{DP} + C_{DI}$ : total drag coefficient
    \item $C_{DP_{tail}} = 0.01$ : parasite drag coefficient of the tail
    \item $C_{DP_{wing}} = 0.0055$ : parasite drag coefficient of the wing
    \item $C_{DI} = \frac{C_{L}^2}{\pi AR}$ : induced drag coefficient
    \item $AR = \frac{b^2}{S}$ : aspect ratio
    \item $L = C_L \cdot \left(\frac{\rho}{2}\right) \cdot V^2 \cdot S$ : Lift force
    \item $D = C_D \cdot \left(\frac{\rho}{2}\right) \cdot V^2 \cdot S$ : Drag force
\end{itemize}


We want that this airplan move the maximum possible bagage per time, from A to D. This airplan may stop in B or C for fuel charging. each stop (in A, B, C, or D) will caues 1.5h. Imaging the cruse speed in 36000ft is 500 mile per hour.

Find:
a) Best path
b) maximum output(pound per day)
c) feul consumption(feul pound per bagae pound to D)
d) with the purpose of more effitiency, redesign the path(minimum the feul consumption(fuel pound per bagae tons to D))

nodes: {A, B, C, D}
edges: {AB: 2000, AC: 4200, AD:7000, BC:2400, BD:5200, CD:3000}


---

How much should be the width of airport Band(باند فرودگاه) that a B757-200 airplan can turn on it(do U-TURN)

--- 

\section{Problem}

The table below presents the profile specifications of a proposed airport runway site. A runway is required for this airport with a \textbf{basic length} of 8000 ft. Apply the following corrections to the runway length:

\begin{itemize}
    \item Add 10\% to the runway length for each 1\% of effective gradient.
    \item Add 7\% to the runway length for every 1000 ft elevation above mean sea level.
\end{itemize}

You are required to design an airport runway at this location in such a way that the FAA regulations are satisfied while minimizing the overall cost. The following cost data are provided:

\begin{itemize}
    \item Pavement cost: \$20 per square foot
    \item Cutting or filling cost: \$0.03 per cubic foot
    \item Borrowing fill material or hauling excess cut material outside the site: \$0.05 per cubic foot
\end{itemize}

Show the ground profile, all calculations, and explain how your design satisfies FAA regulations. (Minor approximations are acceptable.)

\subsection*{Site Profile Data}

\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Station} & \textbf{Elevation (ft)} \\
\hline
0   & 1020 \\
20  & 980  \\
40  & 980  \\
60  & 1000 \\
80  & 1040 \\
100 & 1020 \\
120 & 990  \\
140 & 1000 \\
160 & 1040 \\
\hline
\end{tabular}
\end{table}


---

A sketch of the obstruction surfaces defined in FAR part 77 is shown in Fig. B-1. The obstruction surfaces are to be specified for approaches to a 10,000-ft runway designed for use by transport aircraft for precision-instrument operations. The elevation of the runway is 642.5 ft AMSL.

a. Determine the coordinates of points A, B, C, D, E, F, and G, shown in Fig. B-1.

b. Determine whether an object which is 280 ft high located at a point 12,000 ft from the midpoint of the runway along the extended runway centerline penetrates the FAR part 77 obstruction surfaces.

c. Determine the maximum elevation of a tower located at a point 2000 ft from the midpoint of the runway measured along the runway centerline and offset a distance of 8000 ft from the runway centerline, if it is not to penetrate the FAR part 77 obstruction surfaces.

My answer is:
assuming the x axis to be horizental(along the runway) and y axis is the vertical direction(prependecilar to runway) and z axis is the elevation from ground.

The center point is set to be the mid point of the runway. so the center of runway is (0, 0, 642.5)

Point A is (0, 5000, 642.5+150=792.5) and point B is (0, 5000+4000=9000, 542.5+150+200=992.5) as we assume the slope from A to B is 1:20.

For point C, we can find the slop for changes in y according to x axis with this formula: \frac{(16000/2) - (1000+2*200)}{50,000}. therefore, the C_x = 5000 + 200 + 5000 = 10200 and C_y = 500 + 200 + calculated slop * 5000 = 1360. and C_z = 642.5+150=792.5.

For point G, we know this protected distance is 1000. So it is similare to C with small differences.
G_x = 5000 + 200 + 1000 = 6200 and G_y = 500 + 200 + 132 = 832 and G_z = 642.5 + 150/5 = 672.5.

For point D, we know it is y=0 and x=50,000 + 5000 + 200 = 55200 with z=642.5 + 5000/50 + 45000/40 = 1867.5

For point E, we have same z and y like point D and the y will be 8000. (55200, 8000, 1867.5)

For point F we need only to add to y and z.
F_z = 1867.5 + 5000/7 = 2582 and F_y = E_y + 5000 = 13000.


---

A rough sizing of the airport site is to be made for an airport with parallel runways to be operated in an IFR environment with arrivals on one runway and departures on the other runway. The thresholds of the runways are not staggered. The airside system is to consist of parallel taxiways serving each runway, the terminal complex on one side of the parallel and the property boundary on the other side. The design aircraft is to be a Boeing 767-200. The terminal is to have parallel concourses perpendicular to the runway centerlines, with nose-in aircraft parking. The top of the concourse will be 28 ft high at the end. The runways are 10,000 ft long. A schematic layout of the above facility is shown in Fig.B-8.

a. Determine the separation requirements beween runway centerlines, between the runway centerline and a parallel taxiway centerline, between parallel taxiway centerlines, between the runway and the terminal bnuilding line, between the runway and the propery line, and between concourse faces. Solve this, using the Boeing 767-200 as the design aircraft.

b. Determine the area of the apron surface, in acres, between the concourses if six aircraft are parked on each terminal face.

c. Determine the property area, in acres, between the property line and the terminal building line from ends of the runways.

d. Determine the distance between the runway centerline and the aircraft holding line for rakeoffs.