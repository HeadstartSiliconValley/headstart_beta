// 로그인 상태 체크
function statusChangeCallback(response) { //접속 상태 리턴
  //로그인 상태에 따라서 출력
  if (response.status === 'connected') {  //이미 연결된 상태라면?
    //       console.info(response.authResponse);
    //alert("Your UID is " + response.authResponse.userID);
    getFBdata();
    // getUserPicture(response.authResponse.userID)

    $('#login_text').text('Log-out').attr('href', '#');
  } else {
    $('#login_text').text('Log-in').attr('href', '#modal1');
  }
}

//onlogin 핸들러
function checkLoginState() {
  FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
      });
}


window.fbAsyncInit = function () {
  FB.init({
    appId: '152001685237022', // 페이스북 앱 ID
    status: true, // 로그인 상태
    cookie: true, // 쿠키 허가
    xfbml: true, // xfbml 또는 html5
    version: 'v2.7', // 앱 버전
});
FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
    });
};

// 비동기적으로 SDK 로딩
(function (d, s, id) {
   var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {
     return;
   }
   js = d.createElement(s);
   js.id = id;
   //        js.src = "//connect.facebook.net/en_US/sdk.js";  //Eng.ver
   js.src = "//connect.facebook.net/ko_KR/all.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));

function getFBdata() {
  FB.api('/me', {fields: 'email, gender, name, age_range, link, locale, picture, timezone,verified'}, function(user) {
      console.log(user);
  });
}
function getUserPicture(user_id) {
  FB.api(
      "/" + user_id + "/picture?type=large&redirect=true",
      function (response) {
        if (response && !response.error) {
          $('#profilepic').attr('src', response.data.url);
          $.post("saveimages",
          {
            url: response.data.url,
            fid: user_id
          },
          function (data, status) {
            $('#profilepic').attr('src', data);
          });
        }
      });
}
