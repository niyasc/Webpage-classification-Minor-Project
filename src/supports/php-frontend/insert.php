<?php
	require("./config.php");
	if($_SERVER["REQUEST_METHOD"] == "POST")
	{
		if(empty($_POST["url"]))
		{
			header("Location: index.php?message=url+cannot+be+empty&category=".$_POST["category"]);
		}
		else
		{
			query("insert into sitelist(url,category) values(?,?)",$_POST["url"],$_POST["category"]);
			$count=query("select count(*) from sitelist");
			header("Location: index.php?message=record+added&category=".$_POST["category"]);
		}
	}
	else 
		header("Location: index.php");
?>
