using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MailKit.Net.Imap;
using MailKit;

namespace Email_AttachmentExec
{
    class Program
    {
        static void Main()
        {
            ImapClient client = new ImapClient();
            client.Connect("imap.test.net", 993, true);
            client.Authenticate("username", "password");
            // string[] words = str.Split(new char[] {' '});
            //for (int i = 0; i < words.Length - 1; i++)
            //{
            //    if (words[i].Equals("not"))
            //        wordsBesideNot.Add(words[i + 1]);
            //}
        }
    }
}
