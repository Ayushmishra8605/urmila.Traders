import streamlit as st
STYLE ="""
<style>
/* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
}

/* Body */
body {
    background-color: #f4f6f9;
    color: #333;
    line-height: 1.6;
}

/* Header */
header {
    background: #0a1f44;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    font-size: 28px;
    letter-spacing: 1px;
}

/* Navigation */
nav {
    background: #132f63;
    padding: 10px 0;
}

nav ul {
    list-style: none;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}

nav ul li a:hover {
    color: #ffcc00;
}

/* Hero Section */
.hero {
    background: linear-gradient(rgba(10,31,68,0.8), rgba(10,31,68,0.8)),
                url('trading-bg.jpg') no-repeat center center/cover;
    color: white;
    padding: 80px 20px;
    text-align: center;
}

.hero h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.btn {
    display: inline-block;
    padding: 10px 25px;
    background: #ffcc00;
    color: #000;
    text-decoration: none;
    font-weight: bold;
    border-radius: 5px;
    transition: 0.3s;
}

.btn:hover {
    background: #e6b800;
}

/* Services Section */
.services {
    padding: 50px 20px;
    text-align: center;
}

.services h2 {
    margin-bottom: 30px;
    font-size: 28px;
    color: #0a1f44;
}

.service-box {
    display: inline-block;
    width: 30%;
    background: white;
    margin: 10px;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.service-box h3 {
    margin-bottom: 10px;
    color: #132f63;
}

/* Footer */
footer {
    background: #0a1f44;
    color: white;
    text-align: center;
    padding: 15px 0;
    margin-top: 30px;
}"""