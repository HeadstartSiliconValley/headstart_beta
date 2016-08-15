var imported = document.createElement('script');
imported.src = 'https://static.nid.naver.com/js/naverLogin_implicit-1.0.2.js';
document.head.appendChild(imported);

var naver_id_login = new naver_id_login("rclICSzU14AW3Z1ewwsS", "http://www.headstartsv.com");
var state = naver_id_login.getUniqState();

naver_id_login.setButton("green", 3, 33);
naver_id_login.setDomain(".headstartsv.com");
naver_id_login.setState(state);
//naver_id_login.setPopup();
naver_id_login.init_naver_id_login();

