$(function () {
	$(".submit").click(function () {
		var name = $(".name").val();

		var data = {
			name: name
		};
		//console.log(JSON.stringify(data));
		$.ajax({
			url: '../login',
			data: JSON.stringify(data),
			//dataType: 'json',
			contentType: 'application/json',
			type: "POST",
			success: function (data) {
				window.location.href = '../login/'+data;
			},
			error: function (XMLHttpRequest, textStatus, errorThrown) {
				alert("error!");
			}
		});
	});
});