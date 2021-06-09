using System;
using System.Diagnostics;
using System.Threading;

namespace Kill_SuspectProcess
{
    class Program
    {
        static void Main()
        {
            string[] suspect_procnames = { "beacon", "meterpreter", "payload", "notepad" };

            while (true)
            {
                Process[] processes = Process.GetProcesses();

                foreach (Process process in processes)
                {
                    foreach (string suspect_procname in suspect_procnames)
                    {
                        if (process.ProcessName.Contains(suspect_procname))
                        {
                            process.Kill();
                        }
                    }
                }
                Thread.Sleep(1000 * 5);
            }
        }
    }
}
