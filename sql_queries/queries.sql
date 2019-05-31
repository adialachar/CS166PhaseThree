
--LIST NUMBER OF AVAILABLE SEATS FOR GIVEN FLIGHT--
SELECT DISTINCT P.seats
FROM FlightInfo FI, Flight F, Plane P
WHERE FI.flight_id = /*flight var*/ AND F.actual_departure_date = /* date var*/ AND P.id = FI.plane_id
-
SELECT num_sold
FROM Flight
WHERE fnum = /*flight var*/;

--LIST NUMBER OF REPAIRS PER PLANE IN DESCENDING ORDER--
SELECT COUNT(R.rid) AS mycount, P.id
FROM Plane P, Repairs R
WHERE R.plane_id = P.id
GROUP BY P.id;

--LIST NUMBER OF REPAIRS PER YEAR IN ASCENDING ORDER --
SELECT date_part('year', R1.repair_date) AS R_year, COUNT(R2.id) AS myCount
FROM Repairs R1, Repairs R2
WHERE R1.id = R2.id
GROUP BY R_year;
ORDER BY myCount ASC;

--FIND TOTAL NUMBER OF PASSENGERS WITH GIVEN STATUS--
SELECT COUNT(*)
FROM Reservation R
WHERE R.fid = /*reservation id input*/ AND R._status = /*seat status*/;

