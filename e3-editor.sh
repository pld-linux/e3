#!/bin/sh
E3_DEFAULT=e3vi

case $0 in
   *ws|*wordstar) E3=e3ws ;;
   *vi) E3=e3vi ;;   
   *em|*emacs) E3=e3em ;;
   *pi|*pico) E3=e3pi ;;
   *ne) E3=e3ne ;;
   *) E3="$E3_DEFAULT" ;;
esac

exec "$E3" "$@"
