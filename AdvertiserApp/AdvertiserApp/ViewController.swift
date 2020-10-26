//
//  ViewController.swift
//  AdvertiserApp
//
//  Created by PubMatic on 18/10/20.
//

import UIKit
import StoreKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func updateConversionValueAction() {
        
        // Apps that are advertised by an ad network campaign call this method or registerAppForAdNetworkAttribution() when the app first launches. They may call updateConversionValue(_:) again within a rolling 24-hour period to update the conversion value. Calling this method serves two purposes:
        
        // It generates an install notification, which is the cryptographically signed data validating that a user installed and launched this app as a result of an ad.
        
        // It enables the app to provide and update a conversion value.
        SKAdNetwork.updateConversionValue(3)
        NSLog("Conversion Value Updated!")
    }

}

