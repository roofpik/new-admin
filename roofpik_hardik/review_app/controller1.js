var app = angular.module('myApp', []); // app module defination 
app.controller('ReviewCtrl', function($scope, $http, $timeout) { //defining Review controller

    var x = "",
        y = ""; // string appending variables for html of view

    var $grid = $('.grid').masonry({ // masonry initialization on grid class of view
        columnWidth: 300, // having column width of 300
        itemSelector: '.grid-item' // applying on grid-tem class  
    });
    var mload = function() {
        $timeout(function() {
            $grid.masonry(); // reload the masonry
        }, 500)
    }
    $scope.last = 1;
    var func1 = function(response) {
            $scope.data = response.data.items;
            y = "";
            console.log($scope.data)
            for (var i = 0; i < $scope.data.length; i++) {

                html = '<div class="card"><div class="card-image"><img src="scenery.jpg"><span class="card-title">' + $scope.data[i].uname + '</span></div><div class="card-content"><span class="more">' + $scope.data[i].detail + '</span></div></div>';
                y = y + '<div class="grid-item">' + html + '</div>';
            }
            //  console.log($scope.data)


            //console.log(y);
            var z = y;
            // console.log(z);
            var $moreBlocks = $(z);
            // console.log($moreBlocks);
            $grid.append($moreBlocks);
            $grid.masonry('appended', $moreBlocks);
            x = 0;
            $timeout(function() {
                $(document).ready(function() {
                    // Configure/customize these variables.


                    $('.more').each(function() {
                        var content = $(this).html();

                        if (content.length > showChar) {

                            var c = content.substr(0, showChar);
                            var h = content.substr(showChar, content.length - showChar);

                            var html = c + '<span class="moreellipses">' + ellipsestext + '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a class="morelink">' + moretext + '</a></span>';

                            $(this).html(html);
                        }

                        $(this).removeClass('more');

                    });


                });
            }, 0);
        } // pagination variable for api call 

    var a1 = 0; // flag variable for limiting http requests 
    if (a1 == 0) {
        a1 = 1;
        //console.log(a1)
        $timeout(function() { // timeout service for calling http service into it
            $http.get("http://localhost:80/v1/repeat_review?pkey=-KYJONgh0P98xoyPPYm9&pagination=1").then(function(response) { // http service for the first time without scroll
                func1(response);
                mload();
            });
            //console.log($scope.var)


        }, 0)
    }

    var showChar = 100; // How many characters are shown by default
    var ellipsestext = "...";
    var moretext = "Show more >";
    var lesstext = "Show less";



    $(".grid").on("click", ".morelink", function() { // on clicking more link class 
        console.log('HDK')

        if ($(this).hasClass("less")) { // if less class is present  then remove less and put moretext 
            $(this).removeClass("less");
            $(this).html(moretext);
            mload();
        } else {
            $(this).addClass("less"); // else add less class 

            $(this).html(lesstext); // put less text
            mload();
        }
        $(this).parent().prev().toggle(); // ttoggling the css
        $(this).prev().toggle();
        return false;
    });


    var getDataset = function() {
        console.log('In func')
        $scope.last = $scope.last + 1;
        var x = 0;

        if (x == 0) {
            x = 1;

            $timeout(function() {

                console.log("http://localhost:80/v1/repeat_review?pkey=-KYJONgh0P98xoyPPYm9&pagination=" + $scope.last.toString())
                $http.get("http://localhost:80/v1/repeat_review?pkey=-KYJONgh0P98xoyPPYm9&pagination=" + $scope.last.toString()).then(function(response) {
                    func1(response);
                    mload();
                });
            }, 0)

        }

    }



    window.addEventListener('scroll', function() {


        if (window.scrollY === document.body.scrollHeight - window.innerHeight) {

            getDataset();
            mload();
            console.log('1111');

        }

    });




});
