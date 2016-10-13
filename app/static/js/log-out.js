$(function () {
	$(".sign-out").click(function () {
		$.ajax({
			url: '../logout',
			data: {},
			dataType: 'json',
			contentType: 'application/json',
			type: "POST",
			success: function (data) {
				if (data.success) {
					window.location.href = '../';
				}
				else {
					alert(data.msg);
				}
			},
			error: function (XMLHttpRequest, textStatus, errorThrown) {
				alert("Request error!");
			}
		});
	});
});