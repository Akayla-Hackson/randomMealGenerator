		function send_form(){
                        $.post("/open_api/login", { "username":$('#user').val(), "password":$('#password').val()},
                                function(data, textStatus) {
                                        //this gets called when browser receives response from server
                                        console.log(data.token);
                                        jwt = data.token;
                                        console.log(data);
                                        noError();
                                        goToMainPage();
                                        //make secure call with the jwt

                                }, "json").fail( function(response) {
                                        //this gets called if the server throws an error
                                        console.log("error");
                                        displayError();
                                        console.log(response);
                                });
                        return false;
                }
                
                function displayError(){
                        var loginError = document.getElementById("loginError");
                        loginError.style.display = "block";
                }
                
                function noError(){
                        var loginError = document.getElementById("loginError");
                        loginError.style.display = "none";
                }
		function reset() {
			document.getElementById('SlotImage1').src = "https://www.sourcecodester.com/sites/default/files/question.jpg";
                        document.getElementById('SlotImage2').src = "https://www.sourcecodester.com/sites/default/files/question.jpg";
                        document.getElementById('SlotImage3').src = "https://www.sourcecodester.com/sites/default/files/question.jpg";
		}
                function goToMainPage(){
			reset();
                        var signDisplay = document.getElementById("signDisplay");
                        signDisplay.style.display = "none";
                        var stage = document.getElementById("stage");
                        stage.style.display = "block";
                        var spin = document.getElementById("spin");
                        spin.style.display = "block";
                        var protein = document.getElementById("protein");
                        protein.style.display = "block";
                        var veggie = document.getElementById("veggie");
                        veggie.style.display = "block";
                        var carbs = document.getElementById("carbs");
                        carbs.style.display = "block";
                        var again = document.getElementById("again");
                        again.style.display = "none";
                        var veg = document.getElementById("vegitarian");
                        veg.style.display = "block"
                        var vLabel = document.getElementById("vLabel");
                        vLabel.style.display = "block"
                        var refreshButton = document.getElementById("refreshButton");
                        refreshButton.style.display = "block";
                        var checkOut = document.getElementById("checkOut");
                        checkOut.style.display = "none";
                        var thanks = document.getElementById("thanks");
			thanks.style.display = "none";
			var body2 = document.getElementById("body2");
                        body2.style.display = "block";
		}
		function restyle()
                {
                        var signupContainer = document.getElementById("signDisplay");
                        signupContainer.style.display = "none";
                        var refreshButton = document.getElementById("refreshButton");
                        refreshButton.style.display = "block";
                        var stage = document.getElementById("stage");
                        stage.style.display = "none";
                        var spin = document.getElementById("spin");
                        spin.style.display = "none";
                        var protein = document.getElementById("protein");
                        protein.style.display = "none";
                        var veggie = document.getElementById("veggie");
                        veggie.style.display = "none";
                        var carbs = document.getElementById("carbs");
                        carbs.style.display = "none";
                        var again = document.getElementById("again");
                        again.style.display = "none";
                        var veg = document.getElementById("vegitarian");
                        veg.style.display = "none"
                        var vLabel = document.getElementById("vLabel");
                        vLabel.style.display = "none"
                        var checkOut = document.getElementById("checkOut");
                        checkOut.style.display = "none";
                        var thanks = document.getElementById("thanks");
                        thanks.style.display = "block";
			var body2 = document.getElementById("body2");
                        body2.style.display = "block";
                	reset();
		}
                function getLoginPage()
                {
			reset();
                        var signupContainer = document.getElementById("signDisplay");
                        signupContainer.style.display = "block";
                        var refreshButton = document.getElementById("refreshButton");
                        refreshButton.style.display = "none";
                        var stage = document.getElementById("stage");
                        stage.style.display = "none";
                        var spin = document.getElementById("spin");
                        spin.style.display = "none";
                        var protein = document.getElementById("protein");
                        protein.style.display = "none";
                        var veggie = document.getElementById("veggie");
                        veggie.style.display = "none";
                        var carbs = document.getElementById("carbs");
                        carbs.style.display = "none";
                        var again = document.getElementById("again");
                        again.style.display = "none";
                        var veg = document.getElementById("vegitarian");
                        veg.style.display = "none";
                        var vLabel = document.getElementById("vLabel");
                        vLabel.style.display = "none";
                        var checkOut = document.getElementById("checkOut");
                        checkOut.style.display = "none";
                        var thanks = document.getElementById("thanks");
                        thanks.style.display = "none";
			var body2 = document.getElementById("body2");
                        body2.style.display = "block";
                }
                function get_mProtein(){
                        //make secure call with the jwt
                        secure_get_with_token("/secure_api/get_mProtein",{ },
                                 function(data){
                                         console.log("got meats");
                                         console.log(data)
                                         var arrayLength = 5;
                                         var allMeat = [arrayLength];
                                         for (var i = 0; i < data.meat.length; i++) {
                                                var object = data.meat[i];
                                                allMeat[i] = object;
                                                for (property in object) {
                                                        var value = object[property];
                                                }
                                        }
                                        document.getElementById('murl1').setAttribute("src", allMeat[0][1]);
                                        document.getElementById('murl2').setAttribute("src", allMeat[1][1]);
                                        document.getElementById('murl3').setAttribute("src", allMeat[2][1]);
                                        document.getElementById('murl4').setAttribute("src", allMeat[3][1]);
                                        document.getElementById('murl5').setAttribute("src", allMeat[4][1]);
                                 },
                                 function(err){
                                         console.log(err)
                                 });
                }
                function get_vProtein(){
                        secure_get_with_token("/secure_api/get_vProtein",{ }, 
                                                function(data){
                                                        console.log("got vProtein"); 
                                                        console.log(data)
                                                        var arrayLength = 5;
                                                        var allvProtein = [arrayLength];
                                                        for (var i = 0; i < data.vegPro.length; i++) {
                                                                var object = data.vegPro[i];
                                                                allvProtein[i] = object;
                                                                for (property in object) {
                                                                        var value = object[property];
                                                                }       
                                                        }
                                                        document.getElementById('vPurl1').setAttribute("src", allvProtein[0][1]);
                                                        document.getElementById('vPurl2').setAttribute("src", allvProtein[1][1]);
                                                        document.getElementById('vPurl3').setAttribute("src", allvProtein[2][1]);
							document.getElementById('vPurl4').setAttribute("src", allvProtein[3][1]);
                                                        document.getElementById('vPurl5').setAttribute("src", allvProtein[4][1]);
                                                },
                                                function(err){ 
                                                        console.log(err) 
                                        });
                }
                function get_veggie(){
                        secure_get_with_token("/secure_api/get_veggie",{ }, 
                                                function(data){
                                                        console.log("got veggies"); 
                                                        console.log(data)
                                                        var arrayLength = 5;
                                                        var allVeggies = [arrayLength];
                                                        for (var i = 0; i < data.veg.length; i++) {
                                                                var object = data.veg[i];
                                                                allVeggies[i] = object;
                                                                for (property in object) {
                                                                        var value = object[property];
                                                                }       
                                                        }
                                                        document.getElementById('vegurl1').setAttribute("src", allVeggies[0][1]);
                                                        document.getElementById('vegurl2').setAttribute("src", allVeggies[1][1]);
                                                        document.getElementById('vegurl3').setAttribute("src", allVeggies[2][1]);
                                                        document.getElementById('vegurl4').setAttribute("src", allVeggies[3][1]);
                                                        document.getElementById('vegurl5').setAttribute("src", allVeggies[4][1]);
                                                },
                                                function(err){ 
                                                        console.log(err) 
                                        });
                }
                function get_carbs(){
                        secure_get_with_token("/secure_api/get_carbs",{ }, 
                                                function(data){
                                                        console.log("got carbs"); 
                                                        console.log(data)
                                                        var arrayLength = 5;
                                                        var allCarbs = [arrayLength];
                                                        for (var i = 0; i < data.carbs.length; i++) {
                                                                var object = data.carbs[i];
                                                                allCarbs[i] = object;
                                                                for (property in object) {
                                                                        var value = object[property];
                                                                }       
                                                        }
                                                        document.getElementById('curl1').setAttribute("src", allCarbs[0][1]);
                                                        document.getElementById('curl2').setAttribute("src", allCarbs[1][1]);
                                                        document.getElementById('curl3').setAttribute("src", allCarbs[2][1]);
                                                        document.getElementById('curl4').setAttribute("src", allCarbs[3][1]);
                                                        document.getElementById('curl5').setAttribute("src", allCarbs[4][1]);
                                                },
                                                function(err){ 
                                                        console.log(err) 
                                        });
                }
                function DoSpin() {
			var checkBox = document.getElementById("vegitarian");
                                if(checkBox.checked == true){
                                        get_vProtein();
                                        var edamame = document.getElementById("vPurl1");
                                        var lentils = document.getElementById("vPurl2");
                                        var tofu = document.getElementById("vPurl3");
                                        var beans = document.getElementById("vPurl4");
                                        var seitan = document.getElementById("vPurl5");
                                        var slot1images = [ edamame, lentils, tofu, beans,seitan];
                                        //keys: 0=edamame, 1=lentils , 2=tofu , 3=beans, 4=seitan
                                }
                                else {
                                        get_mProtein();
                                        var chicken = document.getElementById("murl1");
                                        var steak = document.getElementById("murl2");
                                        var sausage = document.getElementById("murl3");
                                        var meatloaf = document.getElementById("murl4");
                                        var lamb = document.getElementById("murl5");
                                        var slot1images = [ chicken, steak, sausage, meatloaf,lamb];
                                        //keys: 0=chicken, 1=steak , 2=sausage , 3=meatloaf, 4=lamb
                                }
                                get_veggie();
                                var broc = document.getElementById("vegurl1");
                                var carrot = document.getElementById("vegurl2");
                                var greenBean = document.getElementById("vegurl3");
                                var eggplant = document.getElementById("vegurl4");
                                var spinach = document.getElementById("vegurl5");
                                var slot2images = [broc,carrot,greenBean,eggplant,spinach];
                                //keys: 0=broc, 1=carrot, 2=greenBean , 3=eggplant, 4=spinach


                                get_carbs();
                                var mac = document.getElementById("curl1");
                                var fries = document.getElementById("curl2");
                                var rice = document.getElementById("curl3");
                                var noodles = document.getElementById("curl4");
                                var bread = document.getElementById("curl5");
                                var slot3images = [mac,fries,rice,noodles,bread];
                                //keys: 0=mac, 1=fries , 2=rice , 3=noodles, 4=bread

                                var slotImage1 = Math.floor((Math.random() * 5));
                                var slotImage2 = Math.floor((Math.random() * 5));
                                var slotImage3 = Math.floor((Math.random() * 5));

                                var img1 = slot1images[slotImage1];
                                var img2 = slot2images[slotImage2];
                                var img3 = slot3images[slotImage3];

                                document.getElementById('SlotImage1').src = img1.src;
                                document.getElementById('SlotImage2').src = img2.src;
                                document.getElementById('SlotImage3').src = img3.src;



                                var again = document.getElementById("again");
                                again.style.display = "block";
                                var checkOut = document.getElementById("checkOut");
                                checkOut.style.display = "block";
		}
                function wantMeal() 
                {
                        secure_get_with_token("/secure_api/add_meals",{"slot1Img":$('#SlotImage1').attr('src'), "slot2Img":$('#SlotImage2').attr('src'), "slot3Img":$('#SlotImage3').attr('src')},
                                        function(data){
                                                console.log(data);
						restyle();
                                        },
                                        function(err){ 
                                                console.log(err) 
                                        });
                        return false;
                }

                                                                                                               
