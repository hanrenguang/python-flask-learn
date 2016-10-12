$(function () {
	//登录
	$(".submit").click(function () {
		var username = $("#username").val();
		var password = $("#password").val();

		if(!username) {
			alert("Please enter your username!");
			return;
		}
		else if(!password) {
			alert("Please enter your password!");
			return;
		}

		var data = {
			username: username,
			password: password
		};
		$.ajax({
			url: '../login',
			data: JSON.stringify(data),
			dataType: 'json',
			contentType: 'application/json',
			type: "POST",
			success: function (data) {
				if (data.success) {
					//window.location.href = '../login?user='+data.username;
					window.location.href = '../user';
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