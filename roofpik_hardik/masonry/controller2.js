  var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope, $timeout) {





      $scope.data = {};
      var arrData = [];
      var flag = 0;
      var $grid = $('.grid').masonry({
          columnWidth: 200,
          itemSelector: '.grid-item'
      });

      $scope.st = '-KnOYLXRTPyFYnziowpG';

      var x = "";

      db.ref('posts').orderByKey().limitToFirst(15).once('value', function(snapshot) {
          $timeout(function() {
              $scope.data = snapshot.val();
              console.log($scope.data);
              var y="";
              for (var i in $scope.data) {
                  $scope.st = i;
                  // console.log($scope.data[i])
                  html='<div class="card"><div class="card-image"><img src="scenery.jpg"><span class="card-title">Card Title</span></div><div class="card-content">'+$scope.data[i].review+'</div></div>';
                  y = y + '<div class="grid-item">' + html + '</div>';
                  // arrData.push('<p class="grid-item">' + $scope.data[i].review + '</p>');

              }
              var z=x+y;
              console.log(z);
              var $moreBlocks = $(z);
              $grid.append($moreBlocks);
              $grid.masonry('appended', $moreBlocks);
              $timeout(function(){
                 $grid.masonry();
              }, 500)
             
              // console.log('1');
              // var $elems = $(arrData);
              // $grid.append($elems).masonry('appended', $elems);
              // console.log(arrData)

          }, 0)

          //console.log('2');


      });



      var getDataset = function() {
          db.ref('posts').orderByKey().startAt($scope.st).limitToFirst(15).once('value', function(snapshot) {
              $timeout(function() {
                  $scope.data = snapshot.val();
                  console.log($scope.data);
                  var y="";
                  for (var i in $scope.data) {
                      $scope.st = i;
                      // console.log($scope.data[i])
                   //  html='<div class="row"> <div class="col s12 m5"> <div class="card"> <div class="card-image"> <img src="scenery.jpg"> <span class="card-title">'+$scope.data[i].author+'</span> </div> <div class="card-content"> <p>'+$scope.data[i].review+'</p></div><div class="card-action"><a href="#">'+$scope.data[i].date+'</a></div></div></div></div>';
                 // html='<div class="row"><div class="col s12 m7"><div class="card"><div class="card-image"><img src="scenery.jpg"><span class="card-title">'+$scope.data[i].author+'</span></div><div class="card-content"><p>I am a very simple card. I am good at containing small bits of informationI am convenient because I require little markup to use effectively.</p></div><div class="card-action"><a href="#">This is a link</a></div></div></div></div>';
                 html='<div class="card"><div class="card-image"><img src="scenery.jpg"><span class="card-title">Card Title</span></div><div class="card-content">'+$scope.data[i].review+'</div></div>';

                  y = y + '<div class="grid-item">' + html + '</div>';
                      // arrData.push('<p class="grid-item">' + $scope.data[i].review + '</p>');

                  }
                  var z=x+y;
                  console.log(z);
                  var $moreBlocks = $(z);
                  $grid.append($moreBlocks);
                  $grid.masonry('appended', $moreBlocks);
                  console.log($scope.st);
              }, 0)


              // $('.grid').masonry().masonry('destroy');
              var $elems = $(arrData);
              $grid.append($elems).masonry('appended', $elems).masonry('reloadItems');

          });


      }






      window.addEventListener('scroll', function() {


          if (window.scrollY === document.body.scrollHeight - window.innerHeight-100) {
              if ($scope.flag != $scope.st) {
                  $scope.flag = $scope.st;
                  getDataset();


              }
          }
      });


  });
