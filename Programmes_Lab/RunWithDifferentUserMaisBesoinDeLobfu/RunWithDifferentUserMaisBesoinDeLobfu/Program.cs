using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RunWithDifferentUserMaisBesoinDeLobfu
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            System.Security.SecureString ssPwd = new System.Security.SecureString();
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.FileName = "cmd.exe";
            proc.StartInfo.Domain = "evilbank.local";
            proc.StartInfo.UserName = "Administrateur";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            string password = "pd5Wq.Pqv67er!qw";
            for (int x = 0; x < password.Length; x++)
            {
                ssPwd.AppendChar(password[x]);
            }
            password = "";
            proc.StartInfo.Password = ssPwd;
            proc.Start();
        }
    }
}
