Problem Understanding

The program checks package weights before loading them into a vehicle.
It groups packages based on safety levels such as light, normal, heavy and overload.
After classification, a personalized rule changes the final loading plan.
This helps simulate a safe transport decision system.

Logic / Approach Used

First, I read the user’s name and counted the characters (excluding spaces) to calculate L.
Then I computed PLI = L % 3 to decide which personalized rule should be applied.
Next, I took package weights as input and used loops and conditions to classify them into categories.
Finally, based on the PLI value, some packages were removed or marked invalid and the final loading plan was displayed.

Personalization Applied (Mandatory)

The program uses the PLI (Personalized Logic Index) which depends on my name length.
Name: <Jahnavi Sr>
L value: <10>
PLI value: <1>
Applied Rule: < Rule B >
Rules:

Rule A → Overload packages moved to invalid
Rule B → Very light packages removed
Rule C → Only normal and heavy packages kept

Register Number Logic

Last digit of Register Number = 1
Hence, I applied Rule B (Very Light items removed) logic.

Learning Outcome

I learned how to apply loops and conditional statements to solve a real-world problem.
I understood classification of data and how personalized logic changes program output.
This task also improved my understanding of lists and program flow in Python.
