"""
==================================================
Fuzzy Control Systems: The Cash Allowance System
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

To run program install for python3:
pip3 install scikit-fuzzy
pip3 install matplotlib

The 'cash allowance' is commonly used to illustrate the power of fuzzy logic
principles to generate complex behavior from a compact, intuitive set of
expert rules.

The Cash Allowance System Problem
-----------------------------------

In many companies, awarding bonuses to employees can be subjective and based on variables that are difficult to assess.
Therefore, we are coming up with a proposal to use fuzzy logic for efficient and fair determination of bonuses
for employees in a company.

We would formulate this problem as:

* Inputs
   - `position experience`
      * Universe (year, crisp value range): How many years of experience on current position has an employee,
      on a scale of 0 to 10?
      * Fuzzy set (ie, fuzzy value range): poor, average, good
   - `seniority in company`
      * Universe(year, crisp value range): How many years have the employee worked in our company, on a scale of 0 to 10?
      * Fuzzy set (ie, fuzzy value range): poor, average, good
  - `efficiency`
      * Universe (percent, crisp value range): How many tasks has been done (per month), on a scale of 0 to 120?
      * Fuzzy set: poor, mediocre, average, decent, good

* Outputs
   - `cash allowance`
      * Universe: How much should we appreciate our employee, how high should be cash allowance,
      on a scale of 0% to 50%?
      * Fuzzy set: very low, low, medium, high, very high

* Assumptions:
   - High bonus for the employee with the highest efficiency, but not necessarily high job seniority or seniority
     in our company.
   - Efficiency is the main determinant of cash allowance.
   - The highest cash allowance available only to very experienced, highly efficient employees of the company.
   - Cash allowance distribution prepared in such a way that it motivates employees to increase their work performance
     (high bonus has a higher range) regardless of position experience and seniority in the company.

* Rules
   - IF the *efficiency* was *mediocre*, THEN the *cash allowance* will be very low.
   - IF the *efficiency* was *mediocre* AND (*seniority in company* was *average* OR *position experience*
     was *average*), THEN the cash allowance will be low.
   - IF the *efficiency* was *mediocre* AND (*seniority in company* was *good* OR *position experience* was *good*),
     THEN the cash allowance will be low.
   - IF the *efficiency* was *average* AND *position experience* was *average*,
     THEN the cash allowance will medium.
   - IF the *efficiency* was *average* AND *position experience* was *good*,
     THEN the cash allowance will medium.
   - IF the *efficiency* was *decent* AND (*position experience* was *average* OR *seniority in company* was *good*),
     THEN the cash allowance will be high.
   - IF the *efficiency* was *good* AND (*position experience* was *poor* OR *seniority in company* was *good*),
     THEN the cash allowance will be high.
   - IF the *efficiency* was *good* AND (*position experience* was *poor* OR *seniority in company* was *poor*),
     THEN the cash allowance will be high.
   - IF the *efficiency* was *good* AND *position experience* was *good* AND *seniority in company* was *good*,
     THEN the cash allowance will be very high.

* Usages
   - If I tell this controller that employee has results after a period of cash allowance time:
      * the position experience was 1 year
      * the seniority in company was 1 year
      * the efficiency was 110 percent
   - it would recommend the employee allowance after a period is:
      * a 20% of employee salary.

   - If I tell this controller that employee has results after a period of cash allowance time:
      * the position experience was 5 years
      * the seniority in company was 5 years
      * the efficiency was 30 percent
   - it would recommend the employee allowance after a period is:
      * a 4% of employee salary.

Creating the Cash Allowance Controller Using the skfuzzy control API
----------------------------------------------------------------------

We can use the `skfuzzy` control system API to model this.  First, let's
define fuzzy variables
"""
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
positionExperience = ctrl.Antecedent(np.arange(0, 11, 1), 'positionExperience')
seniorityInCompany = ctrl.Antecedent(np.arange(0, 11, 1), 'seniorityInCompany')
efficiency = ctrl.Antecedent(np.arange(0, 121, 1), 'efficiency')
cashAllowance = ctrl.Consequent(np.arange(0, 51, 1), 'cashAllowance')

# Auto-membership function population is possible with .automf(3, 5, or 7)
positionExperience.automf(3)
seniorityInCompany.automf(3)
efficiency.automf(5)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
cashAllowance['very low'] = fuzz.trimf(cashAllowance.universe, [0, 0, 5])
cashAllowance['low'] = fuzz.trimf(cashAllowance.universe, [0, 5, 10])
cashAllowance['medium'] = fuzz.trimf(cashAllowance.universe, [5, 10, 20])
cashAllowance['high'] = fuzz.trimf(cashAllowance.universe, [10, 20, 30])
cashAllowance['very high'] = fuzz.trimf(cashAllowance.universe, [20, 50, 50])

"""
To help understand what the membership looks like, use the ``view`` methods.
"""

# You can see how these look with .view()
positionExperience.view()
"""
.. image:: PLOT2RST.current_figure
"""
seniorityInCompany.view()
"""
.. image:: PLOT2RST.current_figure
"""
efficiency.view()
"""
.. image:: PLOT2RST.current_figure
"""
cashAllowance.view()
"""
.. image:: PLOT2RST.current_figure

Fuzzy rules
------------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
ten simple rules:

1. If efficiency is mediocre, then the cash allowance is very low.
2. If efficiency is mediocre and seniority in the company or position experience is average, then the cash allowance is low.
3. If efficiency is mediocre and seniority in the company or position experience is good, then the cash allowance is low.
4. If efficiency is average and position experience is average, the cash allowance is medium.
5. If efficiency is average and position experience is good, the cash allowance is medium.
6. If efficiency is mediocre and position experience is good or seniority in the company is good, the cash allowance is medium.
7. If efficiency is decent and position experience is average or seniority in the company is good, the cash allowance is high.
8. If efficiency is decent and position experience is good or seniority in the company is good, the cash allowance is high.
9. If efficiency is good and position experience is poor or seniority in the company is poor, the cash allowance is high.
10. If efficiency is good and position experience is good and seniority in the company is good, the cash allowance is very high.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable cash allowance is a challenge. This is the
kind of task at which fuzzy logic excels.
"""

rule1 = ctrl.Rule(efficiency['mediocre'], cashAllowance['very low'])
rule2 = ctrl.Rule(efficiency['mediocre'] & (seniorityInCompany['average'] | positionExperience['average']),
                  cashAllowance['low'])
rule3 = ctrl.Rule(efficiency['mediocre'] & (seniorityInCompany['good'] | positionExperience['good']),
                  cashAllowance['low'])
rule4 = ctrl.Rule(efficiency['average'] & positionExperience['average'], cashAllowance['medium'])
rule5 = ctrl.Rule(efficiency['average'] & positionExperience['good'], cashAllowance['medium'])
rule6 = ctrl.Rule(efficiency['mediocre'] & (positionExperience['good'] | seniorityInCompany['good']),
                  cashAllowance['medium'])
rule7 = ctrl.Rule(efficiency['decent'] & (positionExperience['average'] | seniorityInCompany['good']),
                  cashAllowance['high'])
rule8 = ctrl.Rule(efficiency['decent'] & (positionExperience['good'] | seniorityInCompany['good']),
                  cashAllowance['high'])
rule9 = ctrl.Rule(efficiency['good'] & (positionExperience['poor'] | seniorityInCompany['poor']), cashAllowance['high'])
rule10 = ctrl.Rule(efficiency['good'] & positionExperience['good'] & seniorityInCompany['good'],
                   cashAllowance['very high'])

"""
.. image:: PLOT2RST.current_figure

Control System Creation and Simulation
---------------------------------------

Now that we have our rules defined, we can simply create a control system
via:
"""

compensation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])

"""
In order to simulate this control system, we will create a
``ControlSystemSimulation``.  Think of this object representing our controller
applied to a specific set of circumstances.  For consumption, this might be compensation
Sharon at the local brew-pub.  We would create another
``ControlSystemSimulation`` when we're trying to apply our ``compensation_ctrl``
for Travis at the cafe because the inputs would be different.
"""

compensation = ctrl.ControlSystemSimulation(compensation_ctrl)

"""
We can now simulate our control system by simply specifying the inputs
and calling the ``compute`` method.  Suppose we rated the positionExperience 1 out of 10
the seniorityInCompany 1 of 10 and efficiency 110 of 120.

-----------------------------------------
CHECK EMPLOYEE'S CASH ALLOWANCE SECTION
-----------------------------------------

"""

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
compensation.input['seniorityInCompany'] = 1
compensation.input['positionExperience'] = 1
compensation.input['efficiency'] = 120

# Crunch the numbers
compensation.compute()

"""
Once computed, we can view the result as well as visualize it.
"""

number = compensation.output['cashAllowance']
formatted_number = "{:.1f}".format(number)
print("Computed cash allowance for this employee equals = {}.".format(formatted_number))

cashAllowance.view(sim=compensation)
"""
.. image:: PLOT2RST.current_figure

The resulting suggested cash allowance is **20%**.

Final thoughts
--------------

The power of fuzzy systems is allowing complicated, intuitive behavior based
on a sparse system of rules with minimal overhead. Note our membership
function universes were coarse, only defined at the integers, but
``fuzz.interp_membership`` allowed the effective resolution to increase on
demand. This system can respond to arbitrarily small changes in inputs,
and the processing burden is minimal.
"""
plt.show()
