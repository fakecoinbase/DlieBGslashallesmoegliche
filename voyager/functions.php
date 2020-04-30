<?php
    $file = 'data.json';
    $json = file_get_contents($file);
    $data = json_decode($json,true);

    function getAllAccounts($data)
    {
        $allAccounts = array();

        for($i=0; $i<sizeof($data); $i++)
        {
            if(!in_array($data[$i]["account"], $allAccounts))
                array_push($allAccounts, $data[$i]["account"]);
        }

        return $allAccounts;
    }

    function getEntries($data, $account)
    {
        $entries = array();

        for($i=0; $i<sizeof($data); $i++)
        {
            if($data[$i]["account"]==$account)
                array_push($entries, $data[$i]);
        }

        return $entries;
    }

    function getBalance($data, $account)
    {
        $balance = 0;

        $entries = getEntries($data, $account);

        for($i=0; $i<sizeof($entries); $i++)
        {
            $balance+=$entries[$i]["amount"];
        }
        
        return $balance;
    }

    function getNewID($data)
    {
        $id = 0;

        for($i=0; $i<sizeof($data); $i++)
        {
            if($data[$i]["id"]>$id)
                $id = $data[$i]["id"];
        }

        return $id+1;
    }

    function getEntry($data, $id)
    {
        for($i=0; $i<sizeof($data); $i++)
        {
            if($data[$i]["id"]==$id)
                return $data[$i];
        }
    }

    function saveEntry($data, $id, $name, $amount, $account, $date, $comment, $type)
    {
        for($i=0; $i<sizeof($data); $i++)
        {
            if($data[$i]["id"]==$id)
            {    
                $data[$i]["name"] = $name;
                if($type=="out")
                    $amount = $amount*-1;
                $data[$i]["amount"] = $amount;
                $data[$i]["account"] = $account;
                $data[$i]["date"] = $date;
                $data[$i]["comment"] = $comment;

                file_put_contents('data.json', json_encode($data,true) );
                return;
            }
        }

        $new["id"] = $id;
        $new["name"] = $name;
        if($type=="out")
            $amount = $amount*-1;
        $new["amount"] = $amount;
        $new["account"] = $account;
        $new["date"] = $date;
        $new["comment"] = $comment;
        array_push($data, $new);

        file_put_contents('data.json', json_encode($data,true) );
    }

    function deleteEntry($data, $id)
    {
        for($i=0; $i<sizeof($data); $i++)
        {
            if($data[$i]["id"]==$id)
            {
                $string = json_encode($data,true);
                $string = str_replace(json_encode($data[$i],true), '', $string);
                $string = str_replace(',,', ',', $string);
                $string = str_replace('[,', '[', $string);
                $string = str_replace(',]', ']', $string);
            }
        }

        file_put_contents('data.json', $string );
    }
?>
