var n = 0;
var rent_total = 0,paid_rent_total = 0;
var paid_rent,rent;

function add_total(){
	var table = document.getElementById('shop_table');
	n = int(table.rows.length);

	for(var i = 0;i < n;i++){
		rent = int(table.rows[i].cells[2].innerHTML);
		paid_rent = int(table.rows[i].cells[3].innerHTML);

		rent_total += rent;
		paid_rent_total += paid_rent;
	}

	table.rows[n-1].cells[2].innerHTML = rent_total;
	table.rows[n-1].cells[3].innerHTML = paid_rent_total;


}