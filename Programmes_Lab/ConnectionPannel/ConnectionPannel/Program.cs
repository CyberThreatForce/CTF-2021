using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;


namespace ConnectionPannel
{
    class Program
    {
        static void Main(string[] args)
        {
            ///////////////////////////
            ///  REMOTE SQL TOOLS  ///
            ///////////////////////////

            string sql_request;

            Console.WriteLine("REMOTE SQL TOOLS");
            string connetionString;
            SqlConnection cnn;
            connetionString = @"Data Source=WIN-50GP30FGO75;Initial Catalog=Demodb;User ID=sa;Password=demol23";
            cnn = new SqlConnection(connetionString);
            try
            {
                cnn.Open();
                Console.WriteLine("Connection Openned\nTo leave interpreter enter 'exit'");

                SqlCommand command;
                SqlDataReader dataReader;
                String sql, output = "";

                while(true)
                {
                    Console.WriteLine("SQL -> ");
                    sql_request = Console.ReadLine();

                    if(sql_request == "exit")
                    {
                        break;
                    }
                    else
                    {
                        command = new SqlCommand(sql_request, cnn);
                        dataReader = command.ExecuteReader();
                        while (dataReader.Read())
                        {
                            output = output + dataReader.GetValue(0) + " - " + dataReader.GetValue(1) + "\n";
                        }
                        Console.WriteLine("Response : \n" + output);
                    }

                }
            }
            catch
            {
                Console.WriteLine("ERROR TO CONNECT");
            }

        }
    }
}
