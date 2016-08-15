
var imported1 = document.createElement('script');
imported1.type = "text/javascript";
imported1.src = 'https://static.nid.naver.com/js/naverLogin_implicit-1.0.2.js';
document.head.appendChild(imported1);

var imported2 = document.createElement('script');
imported2.src = 'http://code.jquery.com/jquery-1.11.3.min.js';
document.head.appendChild(imported2);

	var naver_id_login = new naver_id_login("rclICSzU14AW3Z1ewwsS", "http://www.headstartsv.com");
        var state = naver_id_login.getUniqState();
        naver_id_login.setButton("green", 2,33);
        naver_id_login.setDomain(".headstartsv.com");
        naver_id_login.setState(state);
 //       naver_id_login.setPopup();
        naver_id_login.init_naver_id_login();
        
function naverSignInCallback() {
                // naver_id_login.getProfileData('프로필항목명');
                // 프로필 항목은 개발가이드를 참고하시기 바랍니다.
                //alert(naver_id_login.getProfileData('email'));
                //alert(naver_id_login.getProfileData('nickname'));
                //alert(naver_id_login.getProfileData('age'));
                console.log(naver_id_login.getProfileData);
        }

        // 네이버 사용자 프로필 조회
        naver_id_login.get_naver_userprofile("naverSignInCallback()");
