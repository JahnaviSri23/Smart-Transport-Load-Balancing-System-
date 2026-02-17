About the Program

In this task I created a small loading verification system for a logistics company.
The idea is to check package weights before loading them into a vehicle so that the transport remains balanced and safe.

The program first reads my name and a list of package weights.
Then it classifies each package into different load categories and finally applies a personalized rule based on my name length (PLI concept).

Personalization Logic

The behavior of the system changes depending on the length of my name.
L = number of characters in my name (excluding spaces)
PLI = L % 3
My Details
Name: <Jahnavi Sri>
L value: < 10>
PLI value: <1>
Applied Rule: < Rule B >

Weight Categories Used
I divided the packages based on how they affect vehicle balance:
Negative weight → Invalid data
0–5 → Very light parcels
6–25 → Normal load (safe packages)
26–60 → Heavy load (needs careful placement)
Above 60 → Overload (unsafe for transport)

Rules Applied by the System
Rule A (PLI = 0)
Overload packages are rejected and marked invalid.
Rule B (PLI = 1)
Very light packages are removed from the loading plan.
Rule C (PLI = 2)
Only normal and heavy packages are allowed.
Very light and overload packages are rejected.

What the Program Shows
The final output displays:
Name length and PLI value
Which rule was applied
Number of valid packages
Number of affected packages
Final loading distribution
