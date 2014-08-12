/**
 * Created by Taras on 01.08.2014.
 */


function delete_cookies(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};


$("#logout").click(function(){
   delete_cookies('login');
    delete_cookies('pass');
    delete_cookies('_xsrf');
});

$("#create_recept").click(function(){


});
