using System;
using System.Collections.Generic;
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
            proc.StartInfo.UserName = "e.ivazov";
            string password = "Da845d-d$M8a";
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
