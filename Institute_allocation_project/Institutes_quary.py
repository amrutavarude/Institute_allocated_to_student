

1. UNDER WHICH QUOTA SEATS ALLOCATED FOR ROUND 1.
ANS:
    SELECT distinct Allotted_Quota
    FROM amruta_varude.institutes_allocated_round1_1;
 
2. UNDER WHICH QUOTA SEATS ALLOCATED FOR ROUND 2.
ANS:
    SELECT distinct Allotted_Quota
    FROM amruta_varude.institutes_allocated_round2_2;

3. HOW MANY PEAPLES UPGRADED THAIR SEATS IN ROUND 2 ?
ANS:
    select remarks,count(*)as Count_of_Upgraded_remark_in_round_2
    from amruta_varude.institutes_allocated_round2_2
    group by Remarks
    having remarks="Upgraded";

4. HOW MUCH SEATS ALLOTTED FOR FRESH STUDENTS ?
ANS:
    SELECT Remarks,count(*)as Total_seats
    FROM amruta_varude.institutes_allocated_round2_2
    where Remarks="Fresh Allotted in 2nd Round";

5. HOW MUCH PEOPLES REPORTED and not reported FOR ROUND1?
ANS:
    SELECT Remarks,count(*)as Total
    FROM amruta_varude.institutes_allocated_round1_1
    GROUP BY Remarks
    HAVING Remarks in("Reported","Not Reported");

6. TOTAL COUNT OF ALLOTTED INSTITUTES OF TOTAL SEATS ALLOCATED IN ROUND 1.
ANS:
    SELECT Allotted_Institute,count(*)as Total_seats
    FROM amruta_varude.institutes_allocated_round1_1
    GROUP BY Allotted_Institute;

7. TOTAL COUNT OF ALLOTTED INSTITUTES OF TOTAL SEATS ALLOCATED IN ROUND 2.
ANS:
    SELECT Allotted_Institute,count(*)as Total_seats_ALLOTTED_IN_ROUND_2
    FROM amruta_varude.institutes_allocated_round2_2
    GROUP BY Allotted_Institute;

8. TOTAL CATEGORY WISE COUNT IN ROUND 1.
ANS:
    SELECT Alloted_Category,count(*)as Total_count_in_round_1
    FROM amruta_varude.institutes_allocated_round1_1
    group by Alloted_Category;

9. TOTAL CATEGORY WISE COUNT IN ROUND 2.
ANS:
    SELECT Alloted_Category,count(*)as Total_count_in_round_2
    FROM amruta_varude.institutes_allocated_round2_2
    group by Alloted_Category;
    
