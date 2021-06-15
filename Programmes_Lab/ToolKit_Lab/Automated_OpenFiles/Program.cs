using System;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace Automated_OpenFiles
{
    class Program
    {
        public static void ProcKillAndDel(object str)
        {
            if (!string.IsNullOrEmpty((string)str))
            {
                Process p = Process.Start((string)str);
                Thread.Sleep(1000 * 15);
                p.Kill();
                File.Delete((string)str);
            }
        }

        static void Main()
        {
<<<<<<< HEAD
            int sleeptime = 1000 * 17;
            string dir = "dir_enum";
=======
            int sleeptime = 1000 * 120;
            string dir = @"C:\Users\p.loffe\Nextcloud\IT-Support";
            string[] files = Directory.GetFileSystemEntries(dir, "*", SearchOption.AllDirectories);
>>>>>>> 95ada178c62dcc5381d54701193d252f0fdb55cf

            while (true)
            {
                string[] files = Directory.GetFiles(dir, "*");

                foreach (string file in files)
                {
                    if (Directory.Exists(file))
                        continue;
                    Thread aThread = new Thread(new ParameterizedThreadStart(ProcKillAndDel));
                    aThread.Start(file);
                }
                Thread.Sleep(sleeptime);
            }
        }
    }
}
