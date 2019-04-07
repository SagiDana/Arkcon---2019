using System;
using System.Reflection;
using Microsoft.AspNetCore.Mvc;

namespace CsharpCoreCTF.Controllers
{
    [Route("Challenge/[controller]")]

    public class CTF : Controller
    {
        [HttpGet]
        public string Get([FromQuery]int i, [FromQuery]string a, [FromQuery]string b, [FromQuery]string c)
        {
            try
            {

                FlagKeeper flagKeeper = new FlagKeeper();

                unsafe
                {
                    int* ptr = flagKeeper.GetFlag(a, c, b);
                    char* flgPTR = (char*)ptr;
                    return (flgPTR[i] ^ (char)i).ToString();
                }

            }
            catch (Exception)
            {
                return "No flag here...";
            }

        }


        public class FlagKeeper
        {
            string _flag = "?";

            private FlagRetriever _flagRetriever;

            unsafe public int* GetFlag(string c, string b, string a)
            {
                _flagRetriever = new FlagRetriever();
                Pointer res = (Pointer)((_flagRetriever.GetType()).GetMethod(c).Invoke(_flagRetriever, new[] { a, b })); ;
                return (int*)Pointer.Unbox(res);
            }

            public unsafe class FlagRetriever
            {
                public int* WTF(string a, string b)
                {
                    Type ftype = Type.GetType($"CsharpCoreCTF.Controllers{a}");
                    var inst = Activator.CreateInstance(ftype);

                    unsafe
                    {

                        var p = inst.GetType().GetField(b, (BindingFlags)(16 | 32 | 4));
                        string pStr = (string)(p.GetValue(inst));
                        fixed (char* pRet = pStr)
                        {
                            return (int*)pRet;
                        }
                    }

                }

            }
        }
    }

}
