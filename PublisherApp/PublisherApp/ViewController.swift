//
//  ViewController.swift
//  PublisherApp
//
//  Created by PubMatic on 18/10/20.
//

import UIKit

class ViewController: UIViewController , POBBannerViewDelegate{

    let owAdUnit = "OpenWrapBannerAdUnit"
    let pubId = "156276"
    let profileId: NSNumber = 1165
    
    var bannerView: POBBannerView?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Create a banner view
        // For test IDs refer - https://community.pubmatic.com/x/IAI5AQ#TestandDebugYourIntegration-TestProfile/Placement
        self.bannerView = POBBannerView(publisherId: pubId, profileId: profileId, adUnitId: owAdUnit, adSizes: [POBAdSizeMake(320, 50)])
        // Set the delegate
        self.bannerView?.delegate = self
        
        // Add the banner view to your view hierarchy
        addBannerToView(banner: self.bannerView!, adSize: CGSize(width: 320, height: 50))
        // Load Ad
        
        self.bannerView?.request.adServerURL = "http://0.0.0.0:8080/rtb/2.5"
    }
    
    @IBAction func showAdAction(_ btn : UIButton) -> Void {
        self.bannerView?.loadAd()
    }
    
    func addBannerToView(banner : POBBannerView?, adSize : CGSize) -> Void {
        
        bannerView?.translatesAutoresizingMaskIntoConstraints = false
        if let bannerView = bannerView {
            view.addSubview(bannerView)
        }
        
        bannerView?.heightAnchor.constraint(equalToConstant: adSize.height).isActive = true
        bannerView?.widthAnchor.constraint(equalToConstant: adSize.width).isActive = true
        
        if #available(iOS 11.0, *) {
            let guide = self.view.safeAreaLayoutGuide
            bannerView?.bottomAnchor.constraint(equalTo: guide.bottomAnchor).isActive = true;
            bannerView?.centerXAnchor.constraint(equalTo: guide.centerXAnchor).isActive = true
        } else {
            let margins = self.view.layoutMarginsGuide
            bannerView?.bottomAnchor.constraint(equalTo: margins.topAnchor).isActive = true;
            bannerView?.centerXAnchor.constraint(equalTo: margins.centerXAnchor).isActive = true
        }
    }
    
    // MARK: - Banner view delegate methods
    //Provides a view controller to use for presenting model views
    func bannerViewPresentationController() -> UIViewController {
        return self
    }
    // Notifies the delegate that an ad has been successfully loaded and rendered.
    func bannerViewDidReceiveAd(_ bannerView: POBBannerView) {
        print("Banner : Ad received with size \(String(describing: bannerView.creativeSize())) ")
    }
    
    // Notifies the delegate of an error encountered while loading or rendering an ad.
    func bannerView(_ bannerView: POBBannerView,
                    didFailToReceiveAdWithError error: Error?) {
        print("Banner : Ad failed with error : \(error?.localizedDescription ?? "")")
    }
    
    // Notifies the delegate whenever current app goes in the background due to user click
    func bannerViewWillLeaveApplication(_ bannerView: POBBannerView) {
        print("Banner : Will leave app")
    }
    
    // Notifies the delegate that the banner ad view will launch a modal on top of the current view controller, as a result of user interaction.
    func bannerViewWillPresentModal(_ bannerView: POBBannerView) {
        print("Banner : Will present modal")
    }
    // Notifies the delegate that the banner ad view has dismissed the modal on top of the current view controller.
    func bannerViewDidDismissModal(_ bannerView: POBBannerView) {
        print("Banner : Dismissed modal")
    }
    
    deinit {
        bannerView = nil
    }

}

