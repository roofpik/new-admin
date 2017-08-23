  var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope, $timeout) {

      console.log('l');
      $scope.data = {};
      $scope.arrData = [];
      $scope.flag=0;

      $scope.st = '-KnOYLXRTPyFYnziowpG';

      /*function makeid() {
          var text = "";
          var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

          for (var i = 0; i < 5; i++)
              text += possible.charAt(Math.floor(Math.random() * possible.length));

          return text;
      }




      var verbs = [
          ["go to", "goes to", "going to", "went to", "gone to"],
          ["look at", "looks at", "looking at", "looked at", "looked at"],
          ["choose", "chooses", "choosing", "chose", "chosen"]
      ];
      var tenses = [
          { name: "Present", singular: 1, plural: 0, format: "%subject %verb %complement" },
          { name: "Past", singular: 3, plural: 3, format: "%subject %verb %complement" },
          { name: "Present Continues", singular: 2, plural: 2, format: "%subject %be %verb %complement" }
      ];
      var subjects = [
          { name: "I", be: "am", singular: 0 },
          { name: "You", be: "are", singular: 0 },
          { name: "He", be: "is", singular: 1 }
      ];
      var complementsForVerbs = [
          ["cinema", "Egypt", "home", "concert"],
          ["for a map", "them", "the stars", "the lake"],
          ["a book for reading", "a dvd for tonight"]
      ]
      Array.prototype.random = function() {
          return this[Math.floor(Math.random() * this.length)];
      };

      function generate() {
          var index = Math.floor(verbs.length * Math.random());
          var tense = tenses.random();
          var subject = subjects.random();
          var verb = verbs[index];
          var complement = complementsForVerbs[index];
          var str = tense.format;
          str = str.replace("%subject", subject.name).replace("%be", subject.be);
          str = str.replace("%verb", verb[subject.singular ? tense.singular : tense.plural]);
          str = str.replace("%complement", complement.random());
          return str;
      }

       var updates = {};


      // for (i = 0; i < 100; i++) {

      //     var newPostKey = firebase.database().ref().push().key;
      //     var d = new Date().getTime();
      //     var postData = {
      //         author: makeid(),
      //         review: generate(),
      //         id: newPostKey,
      //         date: d
      //     }
         
      //     updates['/posts/' + newPostKey] = postData;
      //     console.log(i)
      // }
      // console.log(updates)
      // db.ref().update(updates);*/
      db.ref('posts').orderByKey().startAt($scope.st).limitToFirst(5).once('value', function(snapshot) {
          $timeout(function() {
              $scope.data = snapshot.val();
              console.log($scope.data);
              for (var i in $scope.data) {
                  $scope.st = i;
                  // console.log($scope.data[i])
                  $scope.arrData.push($scope.data[i]);

              }
              console.log($scope.st);

          }, 0)

          $timeout(function() {
              $('.grid').masonry({
                  itemSelector: '.grid-item',
                  percentPosition: true
              });

              //$('.grid-item').masonry().masonry('destroy');


          }, 500)
      });

      var getDataset = function() {
          db.ref('posts').orderByKey().startAt($scope.st).limitToFirst(5).once('value', function(snapshot) {
              $timeout(function() {
                  $scope.data = snapshot.val();
                  console.log($scope.data);
                  for (var i in $scope.data) {
                      $scope.st = i;
                      $scope.arrData.push($scope.data[i]);

                  }
                  console.log($scope.st);
              }, 0)

              $timeout(function() {
                  $('.grid').masonry({
                      itemSelector: '.grid-item',
                      percentPosition: true
                  });
                  // $('.grid-item').masonry().masonry('destroy');
                  $('.grid').masonry().masonry('destroy');



              }, 500)
          });

      }

      // db.ref('h1').orderByKey().limitToFirst($scope.add).on('value', gotdata, errData);
      /*function(snapshot){
    		console.log('k');
    		$scope.article = snapshot.val();
    		console.log($scope.article);


    	}*/


      /* function gotdata(data) {

           $timeout(function() {
               $scope.data = data.val();

               for (var i in $scope.data) {
                   $scope.fdata[i] = $scope.data[i];
                   console.log($scope.fdata[i]);

               }

               
               console.log($scope.fdata, $scope.add);

           }, 0)


           $timeout(function() {
               $('.grid').masonry({
                   itemSelector: '.grid-item',
                   percentPosition: true
               });

           }, 500)


       }

       function errData(err) {
           console.log('Error');
           console.log(err);

       }*/




      window.addEventListener('scroll', function() {


          if (window.scrollY === document.body.scrollHeight - window.innerHeight) {
              getDataset();
          }
      });


  });

