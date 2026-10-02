from faker import Faker
import random

fake = Faker()

product = fake.word().title() + " Headphones"
price = round(random.uniform(20,100),2)
rating = round(random.uniform(3.5,5.0),1)

original = f"""
<!DOCTYPE html>
<html>

<head>

<title>Original Page</title>

<script>

function openDetails(){{
window.open("viewdetails.html","_blank");
}}

</script>

</head>

<body>

<h2>Products</h2>

<button id="viewButton" onclick="openDetails()">

View Details

</button>

</body>

</html>

"""

details = f"""
<!DOCTYPE html>
<html>

<head>

<title>View Details</title>

<style>

#spinner{{
display:block;
color:red;
font-size:22px;
}}

#content{{
display:none;
}}

</style>

<script>

function loadData(){{

setTimeout(function(){{

document.getElementById("spinner").style.display="none";

document.getElementById("content").style.display="block";

}},3000);

}}

window.onload=loadData;

</script>

</head>

<body>

<div id="spinner">

Loading...

</div>

<div id="content">

<h2 id="productName">{product}</h2>

<p id="price">${price}</p>

<p id="rating">{rating} / 5</p>

</div>

</body>

</html>

"""

with open("originalpage.html","w") as file:
    file.write(original)

with open("viewdetails.html","w") as file:
    file.write(details)

print("Files Created Successfully")