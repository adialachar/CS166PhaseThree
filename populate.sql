----------------------------
-- INSERT DATA STATEMENTS --
----------------------------

COPY Customer (
	id,
	fname,
	lname,
	gtype,
	dob,
	address,
	phone,
	zipcode
)
FROM 'customer.csv'
WITH DELIMITER ',';

COPY Pilot (
	id,
	fullname,
	nationality
)
FROM 'pilots.csv'
WITH DELIMITER ',';

COPY Plane (
	id,
	make,
	model,
	age,
	seats
)
FROM 'planes.csv'
WITH DELIMITER ',';

COPY Technician (
	id,
	full_name
)
FROM 'technician.csv'
WITH DELIMITER ',';

COPY Flight (
	fnum,
	cost,
	num_sold,
	num_stops,
	actual_departure_date,
	actual_arrival_date,
	arrival_airport,
	departure_airport
)
FROM 'flights.csv'
WITH DELIMITER ',';

COPY Reservation (
	rnum,
	cid,
	fid,
	status
)
FROM 'reservation.csv'
WITH DELIMITER ',';

COPY FlightInfo (
	fiid,
	flight_id,
	pilot_id,
	plane_id
)
FROM 'flightinfo.csv'
WITH DELIMITER ',';

COPY Repairs (
	rid,
	repair_date,
	repair_code,
	pilot_id,
	plane_id,
	technician_id
)
FROM 'repairs.csv'
WITH DELIMITER ',';

COPY Schedule (
	id,
	flightNum,
	departure_time,
	arrival_time
)
FROM 'schedule.csv'
WITH DELIMITER ',';
