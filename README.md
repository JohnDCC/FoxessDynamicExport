**The issue:**

FoxEss Forced Discharge requires you to set a discharge wattage. This includes household usage which means you get a clunky setup where you might either:
- Export more than you desire
- Accidentally draw from the grid.

**The solution:**

Keep your Discharge level at max so you can absorb all household peaks, but instead, dynamically adjust your Inverter Export Limit so you can consistently control how much you export.

FoxEss does not allow you to do this simply so we have to make a workaround. The EnergyStats app can do this, but not with intelligent parameters.

This automation will dynamically adjust your output between 6pm and 9pm to work with Globird plans. It will always have some baseline export in order to avhieve the ZeroHero Benefit and will dynamically adjust based on your tolerance levels (SOC Cut) to export more at the end of the export period. This will change your inverter Export Limit at 6pm to a low level of your choosing. At 7.30pm, with the last 90 mins of your free charge period, it'll calculate an amount to export based on your defined SOC cutoff (i.e. 60%) and the max rate you want to export at. This way you'll get the best of both worlds, a guaranteed export, no risk of dipping into the grid and a quasi SOC cutoff point. 

**Requirements:**

- Pyscript
- Foxess HA or Foxess-control (recommended)
**
Setup:**

1. Add Configuration to your config file
2. Add python file to your root folder
3. Add your API (FoxCloud) and Serial Number into the python file
4. Add the automations
5. Adjust times, target SOC, battery size and max watts as desired

**Notes:**

It will overshoot the SOC dependant on your home usage so if 60 is lineball for you, run it a bit higher.
