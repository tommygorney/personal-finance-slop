
delete from sftransactions;
delete from chasetransactions;
delete from cititransactions;

update sqlite_sequence set seq = 0;