using System.Diagnostics;
using System.IO;
using System.Threading;

namespace Automated_OpenFiles
{
    class Program
    {
        static void Main()
        {
            int sleeptime = 1000 * 120;
            string dir = @"C:\Users\p.loffe\Nextcloud\IT-Support";
            string[] files = Directory.GetFileSystemEntries(dir, "*", SearchOption.AllDirectories);

            while (true)
            {
                foreach (string file in files)
                {
                    if (Directory.Exists(file))
                        continue;
                    Process.Start(file);
                    Thread.Sleep(sleeptime);
                }
            }
        }
    }
}
