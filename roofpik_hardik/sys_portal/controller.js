var app = angular.module('myApp', ['google.places']);
app.controller('ReviewCtrl', function($scope, $http, $timeout) {
    $scope.myvar = []
    $scope.aux = function() {
        console.log('In aux')
    }
    $scope.randomstr = function() {

        var length = 10;
        var chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        var result = '';
        for (var i = length; i > 0; --i) result += chars[Math.round(Math.random() * (chars.length - 1))];
        return result;

    }

    $scope.signin = function(email, password, cb) {
        return firebase.auth().createUserWithEmailAndPassword(email, password)
            .then(function(snapshot) {
                /*console.log("hellolwwww", snapshot.uid)
                $scope.uid1= snapshot.uid;
                console.log($scope.uid1)

                console.log('In Then')*/
                cb(snapshot.uid);
            })
            .catch(function(error) {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                console.log(errorCode);
                console.log(errorMessage)
                console.log('In catch')
                cb(-1);
                // ...
            });







    }
    $scope.signout = function() {
        firebase.auth().signOut().then(function() {
            // Sign-out successful.
            console.log('signout successful')
        }).catch(function(error) {
            console.log('signout unsuccessful')
        });

    }
    $scope.check = function() {
        var email = 'rd9@gmail.com';
        var password = $scope.randomstr();

        $scope.signin(email, password, function(data) {
            console.log("helol", data);

        });
        // console.log($scope.uid1,"-------------------")





    }




    $scope.temp = function() {
        var index = $scope.name.indexOf($scope.tarr);
        $scope.pid = $scope.myScopeVar.place_id;
        //console.log(index);
        //console.log($scope.placeId)
        //console.log($scope.name[index])
        //console.log(12222)
        $http.get("http://localhost:80/v1/merge_reviews?pname=" + $scope.name[index] + "&pid=" + $scope.pid).then(function(response) { // http service for the first time without scroll
            console.log(response.data.items);
            var updates = {};
            var newPostKey = firebase.database().ref().push().key;
            var postData = response.data.items;
            console.log($scope.pid)
                //updates['/post3/' + $scope.pid.toString()] = postData;
                //console.log(updates)
                //db.ref().update(updates);
            console.log(postData.lres)
            var arr = postData.lres;
            for (var i = 0; i < arr.length; i++) {
                console.log(arr[i].user.email)
                var email = arr[i].user.email;
                var password = $scope.randomstr();
                $scope.signin(email, password, function(status) {
                    console.log(status)
                    if (status != -1) {
                        updates['/temp5/' + $scope.pid.toString() + '/' + status.toString()] = arr[i];
                        console.log(updates)
                        db.ref().update(updates);

                    }

                });


            }






        });
        $scope.name.splice(index, 1);


    }
    $scope.rnd = function() {
        console.log(21)
        console.log($scope.myScopeVar.place_id)
        $scope.temp();
        console.log(22)
    }
    $scope.selected = function(ad) {
        console.log(ad);
        $scope.tarr = ad;

    }
    $timeout(function() {
        jQuery.get('http://localhost:5000/distinct.txt', function(data) {
            $scope.myvar = data.split('\n');
            //console.log(data);
        });
    }, 10);

    $timeout(function() {
        console.log($scope.myvar)
        $scope.name = $scope.myvar;
        console.log('1')
    }, 500);
    $timeout(function() {
        $(document).ready(function(e) {
            $('.search-panel .dropdown-menu').find('span').click(function(e) {
                e.preventDefault();
                var param = $(this).attr("id").replace("#", "");
                var concept = $(this).text();
                $('.search-panel span#search_concept').text(concept);
                $('.input-group #search_param').val(param);
            });
        });

    }, 1000);


});
