<?php

$flag = "FLAG = CYBERTF{N1C3_K33P_G01NG_4G3NT}";
if (isset($_GET['passwd'])) {

        if (hash("md5", $_GET['passwd']) == '0e514198428367523082236389979035'){
            echo "  Вот ваш код доступа . ~  ".$flag;
        } else {
            echo "Обнаруженная атака";
    }
}
?>
