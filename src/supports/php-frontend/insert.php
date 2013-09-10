<?php    // your database's name
    define("DATABASE", "expense");

    // your database's password
    define("PASSWORD", "");

    // your database's server
    define("SERVER", "localhost");

    // your database's username
    define("USERNAME", "root");
?>
<?php
function query(/* $sql [, ... ] */)
    {
        // SQL statement
        $sql = func_get_arg(0);

        // parameters, if any
        $parameters = array_slice(func_get_args(), 1);

        // try to connect to database
        static $handle;
        if (!isset($handle))
        {
            try
            {
                // connect to database
                $handle = new PDO("mysql:dbname=" . DATABASE . ";host=" . SERVER, USERNAME, PASSWORD);

                // ensure that PDO::prepare returns false when passed invalid SQL
                $handle->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); 
            }
            catch (Exception $e)
            {
                // trigger (big, orange) error
                trigger_error($e->getMessage(), E_USER_ERROR);
                exit;
            }
        }

        // prepare SQL statement
        $statement = $handle->prepare($sql);
        if ($statement === false)
        {
            // trigger (big, orange) error
            trigger_error($handle->errorInfo()[2], E_USER_ERROR);
            exit;
        }

        // execute SQL statement
        $results = $statement->execute($parameters);

        // return result set's rows, if any
        if ($results !== false)
        {
            return $statement->fetchAll(PDO::FETCH_ASSOC);
        }
        else
        {
            return false;
        }
    }
?>
<?php
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
			$count=$count[0]["count(*)"];
			header("Location: index.php?message=record+added&category=".$_POST["category"]."&count=".$count);
		}
	}
	else 
		header("Location: index.php");
?>
