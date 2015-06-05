function s4() {
  return Math.floor((1 + Math.random()) * 0x10000)
             .toString(16)
             .substring(1);
};
function guid() {
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
         s4() + '-' + s4() + s4() + s4();
}
if (window.localStorage) {
    var user_id = window.localStorage.getItem("user_id");
    if (!user_id) {
        user_id = guid();
        window.localStorage.setItem("user_id", user_id);
    }
}

var guidFields = document.getElementsByName("guid");
for(var i = 0; i < guidFields.length; i++)
{
	guidFields.item(i).value = user_id;
}