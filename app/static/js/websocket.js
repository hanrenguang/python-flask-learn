$(function () {
	$(".page-header h1").click(function () {
		var wsurl = "ws://127.0.0.1:5000/websocket";
		var socket = new WebSocket(wsurl, "ws");
		socket.onopen = function (event) {
			socket.send("亲爱的服务器！我连上你啦！"); 
		};
		socket.onmessage = function (event) {
			$(this).html("Hello, "+event.data);
		};
	});
});